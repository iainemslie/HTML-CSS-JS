let lastScrollPos = 0;
let subNavBar = document.getElementById('subNavbar');
let hamburger = document.getElementById('hamburger');
let overlay = document.getElementById('menu-overlay');
let hamburgerIcon = document.getElementById('hamburger-icon');

// Remove subscroll bar if scroll down
document.addEventListener("scroll", () => {
    lastScrollPos = window.scrollY;
    
    if (!overlay.classList.contains('display')) {
        if (lastScrollPos > 40) {
            subNavBar.classList.add('hidden');
        } else {
            subNavBar.classList.remove('hidden');
        }
    }
})

// Display overlay if hamburger icon clicked
hamburger.addEventListener('click', () => {
    overlay.classList.toggle('display');
    subNavBar.classList.add('hidden');

    // Change x-mark on icon
    hamburgerIcon.classList.toggle('fa-xmark');
    hamburgerIcon.classList.toggle('fa-lg');
})