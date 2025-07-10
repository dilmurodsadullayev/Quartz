document.addEventListener('DOMContentLoaded', function() {
    // Hide loader after page is fully loaded
    window.addEventListener('load', function() {
        const loader = document.querySelector('.loader-container');
        loader.classList.add('fade-out');
        
        // Remove loader from DOM after fade-out animation
        setTimeout(() => {
            loader.style.display = 'none';
        }, 500);
    });
}); 