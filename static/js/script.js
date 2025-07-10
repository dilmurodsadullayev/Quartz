// Agar qo'shimcha JavaScript funksiyalari kerak bo'lsa, shu yerga yoziladi.
// Masalan, scroll animatsiyalari yoki boshqa interaktiv elementlar.
// Hozircha Bootstrap carousel o'zi ishlaydi.

document.addEventListener('DOMContentLoaded', function () {
    // Kelajakda JS kodlari uchun
});

// Scroll to Top Button Functionality
const scrollTopBtn = document.getElementById('scrollTopBtn');

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        scrollTopBtn.classList.add('visible');
    } else {
        scrollTopBtn.classList.remove('visible');
    }
});

scrollTopBtn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});