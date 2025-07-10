document.addEventListener('DOMContentLoaded', () => {
    const trailContainer = document.createElement('div');
    trailContainer.id = 'trail-container';
    document.body.appendChild(trailContainer);

    const trails = [];
    const maxTrails = 15;
    let lastX = 0;
    let lastY = 0;
    let mouseSpeed = 0;
    let lastTime = performance.now();

    // Create initial trail elements with varying sizes
    for (let i = 0; i < maxTrails; i++) {
        const trail = document.createElement('div');
        trail.className = 'cursor-trail';
        // Vary the size of each particle
        const size = 6 - (i * 0.2);
        trail.style.width = `${size}px`;
        trail.style.height = `${size}px`;
        trailContainer.appendChild(trail);
        trails.push({
            element: trail,
            x: 0,
            y: 0,
            size: size
        });
    }

    document.addEventListener('mousemove', (e) => {
        const currentTime = performance.now();
        const deltaTime = currentTime - lastTime;
        lastTime = currentTime;

        // Calculate mouse speed
        const dx = e.clientX - lastX;
        const dy = e.clientY - lastY;
        mouseSpeed = Math.sqrt(dx * dx + dy * dy) / deltaTime;

        lastX = e.clientX;
        lastY = e.clientY;
    });

    function animate() {
        // Update trail positions with easing
        for (let i = trails.length - 1; i > 0; i--) {
            const trail = trails[i];
            const prevTrail = trails[i - 1];
            
            // Add some randomness to the movement
            const randomOffset = (Math.random() - 0.5) * 2;
            
            trail.x += (prevTrail.x - trail.x) * 0.3 + randomOffset;
            trail.y += (prevTrail.y - trail.y) * 0.3 + randomOffset;
        }

        // Update first trail position
        trails[0].x = lastX;
        trails[0].y = lastY;

        // Apply positions and effects
        trails.forEach((trail, index) => {
            const element = trail.element;
            element.style.left = `${trail.x}px`;
            element.style.top = `${trail.y}px`;
            
            // Adjust opacity and scale based on mouse speed
            const speedFactor = Math.min(mouseSpeed * 0.1, 1);
            const opacity = 1 - (index / maxTrails) * (1 - speedFactor);
            const scale = 1 + (speedFactor * 0.5);
            
            element.style.opacity = opacity;
            element.style.transform = `translate(-50%, -50%) scale(${scale})`;
            
            // Add fade class to older trails
            if (index > 5) {
                element.classList.add('fade');
            } else {
                element.classList.remove('fade');
            }
        });

        requestAnimationFrame(animate);
    }

    animate();
}); 