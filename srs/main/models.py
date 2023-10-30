from django.db import models
import datetime

# Create your models here.

class CardSet(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CardCategory(models.Model):
    parent_card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    
    name = models.CharField(max_length=255)
    name_ko = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.name_ko}'

class CardContent(models.Model):
    c_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    category = models.ForeignKey(CardCategory, on_delete=models.CASCADE, blank=True, null=True)
    
    word_en = models.CharField(max_length=255)
    word_ko = models.CharField(max_length=255)
    
    association = models.CharField(max_length=255, default='')

    image = models.ImageField(upload_to="images/", blank=True, null=True)
    audio = models.FileField(upload_to="audio/", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.word_en}: {self.word_ko}'

class Card(models.Model):
    card_cont = models.ForeignKey(CardContent, on_delete=models.CASCADE)
    
    variant_choice = [
        ('C', 'Comprehension'),
        ('P', 'Production'),
        ('S', 'Spelling'),
    ]
    
    variant = models.CharField(max_length=1, choices=variant_choice)
    
    created = models.DateTimeField(auto_now_add=True)
    last_time_correct = models.DateTimeField(blank=True, null=True)

    times_seen = models.IntegerField(default=0)
    times_correct = models.IntegerField(default=0)
    times_wrong = models.IntegerField(default=0)

    level = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.card_cont.word_en}: {str(self.variant)}'

    def answered_correct(self):
        self.times_seen += 1
        self.times_correct += 1
        self.level += 1
        self.last_time_correct = datetime.datetime.now()
        
        if self.level==8:
            if not self.completed:
                self.completed = True

        self.save()

    def answered_incorrect(self):
        self.times_seen += 1
        self.times_wrong += 1
        self.level = 1
        self.save()

