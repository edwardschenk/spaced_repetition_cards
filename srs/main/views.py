from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import CardSet, Card
from .forms import CreateNewCardSet, CreateNewCard

from datetime import date, datetime, timedelta
from random import choice

# Create your views here.

def index(response):
    card_sets = CardSet.objects.all()
    return render(response, 'main/home.html', {'card_sets':card_sets})

def flashcards(response, set_name):
    
    if response.method=='POST':
        card_id, result = list(dict(response.POST).keys())[1].split('_')
        prev_card = Card.objects.get(id=card_id)

        if result == 'incorrect':
            prev_card.answered_incorrect()
            return HttpResponseRedirect('')
        elif result == 'correct':
            prev_card.answered_correct()
            return HttpResponseRedirect('')

    korean_set = CardSet.objects.get(name=set_name)
    cards = korean_set.card_set.filter(
        (
        Q(last_time_correct__isnull=True)
        ) | (
        Q(level=1) &
        Q(last_time_correct__date__lte=date.today()-timedelta(days=1))
        ) | (
        Q(level=2) &
        Q(last_time_correct__date__lte=date.today()-timedelta(days=2))
        ) | (
        Q(level=3) &
        Q(last_time_correct__date__lte=date.today()-timedelta(days=3))
        ) | (
        Q(level=4) &
        Q(last_time_correct__date__lte=date.today()-timedelta(days=4))
        ) | (
        Q(level=5) &
        Q(last_time_correct__date__lte=date.today()-timedelta(days=5))
        ) | (
        Q(level=6) &
        Q(last_time_correct__date__lte=date.today()-timedelta(days=6))
        ) | (
        Q(level__gte=7) &
        Q(last_time_correct__date__lte=date.today()-timedelta(days=7))
        )
    )
    random_card = choice(cards)
    return render(response, 'main/flashcards.html', {'card': random_card})

def create_card_set(response):
    if response.method=='POST':
        form = CreateNewCardSet(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            desc = form.cleaned_data['description']
            s = CardSet(name=n, description=desc)
            s.save()
        return HttpResponseRedirect(f'/{s.name}/')
    
    else:
        form = CreateNewCardSet()

    return render(response, 'main/makeset.html', {'form':form})

def card_set(response, set_name):
    card_set = CardSet.objects.get(name=set_name)
    cards = card_set.card_set.all()
    return render(response, 'main/card_set_page.html', 
                  {'SetName':card_set.name, 'cards':cards})

def create_cards(response, set_name):
    card_set = CardSet.objects.get(name=set_name)
    if response.method=='POST':
        form = CreateNewCard(response.POST, response.FILES)

        if form.is_valid():
            card = form.save(commit=False)
            card.card_set = card_set
            card.variant = 'comprehension'
            card.save()
            pk = card.pk 
            for var in ('production', 'spelling'):
                new_card = Card.objects.get(id=pk)
                new_card.pk = None
                new_card.variant = var
                new_card.save()
        return HttpResponseRedirect(f'../../{card_set.name}/')
    else:
        form = CreateNewCard()
        return render(response, 'main/makecards.html', 
                      {'form':form, 'SetName':card_set.name})

