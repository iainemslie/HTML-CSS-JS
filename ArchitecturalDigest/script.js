let lastScrollPos = 0;
let subNavBar = document.getElementById('subNavbar');


document.addEventListener("scroll", () => {
    lastScrollPos = window.scrollY;
    
    if (lastScrollPos > 40) {
        subNavBar.classList.add('hidden');
    } else {
        subNavBar.classList.remove('hidden');
    }

})