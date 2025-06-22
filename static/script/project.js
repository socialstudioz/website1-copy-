let next = document.querySelector('.next');
let prev = document.querySelector('.prev');

next.addEventListener('click', function () {
    let items = document.querySelectorAll('.item');
    document.querySelector('.slide').appendChild(items[0]);
});

prev.addEventListener('click', function () {
    let items = document.querySelectorAll('.item');
    document.querySelector('.slide').prepend(items[items.length - 1]);
});

// Auto Slide
setInterval(() => {
    let items = document.querySelectorAll('.item');
    document.querySelector('.slide').appendChild(items[0]);
}, 5000); // Slide every 5 seconds

/*document.addEventListener("DOMContentLoaded", function() {
  const scrollSpeed = 0.07; // lower = slower
  let scrollPos = window.pageYOffset;

  function smoothScroll() {
    scrollPos += (window.pageYOffset - scrollPos) * scrollSpeed;
    window.scrollTo(0, scrollPos);
    requestAnimationFrame(smoothScroll);
  }
  smoothScroll();
});
ScrollReveal({ 
    reset: true,
    distance: '60px',
    duration: 2000,
    delay: 200
  });

  ScrollReveal().reveal('.reveal-top', { origin: 'top' });
  ScrollReveal().reveal('.reveal-bottom', { origin: 'bottom' });
  ScrollReveal().reveal('.reveal-left', { origin: 'left' });
  ScrollReveal().reveal('.reveal-right', { origin: 'right' });*/
ScrollReveal({
    reset: false,
    distance: '60px',
    duration: 1500,
    delay: 200
});

ScrollReveal().reveal('.section-title', { delay: 300, origin: 'top' });
ScrollReveal().reveal('.experience-cards .card', { interval: 200, origin: 'bottom' });
ScrollReveal().reveal('.experience-footer', { delay: 500, origin: 'bottom' });


