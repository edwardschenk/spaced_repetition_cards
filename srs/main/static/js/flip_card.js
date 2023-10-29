// Get card element
const card = document.querySelectorAll('.flip-card');

// Loop through cards. 
// This is so you can have multiple cards on a page.
for (let i = 0; i < card.length; i++) {
   // Add a click event listener to each card.
   card[i].addEventListener("click", function() {
     // Toggle active class on card
     card[i].classList.toggle("active");
   });
}