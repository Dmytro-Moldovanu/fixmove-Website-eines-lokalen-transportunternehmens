document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                let additionalOffset = 0;
                
                // Special adjustment for services section
                if (targetId === '#services') {
                    additionalOffset = -navbarHeight;
                }
                // For möbeltaxi section
                else if (targetId === '#moebeltaxi') {
                    additionalOffset = -navbarHeight - 0;
                }
                // For about section
                else if (targetId === '#about') {
                    additionalOffset = -navbarHeight - 0;
                }
                // For contact section
                else if (targetId === '#contact') {
                    additionalOffset = -20;
                }
                
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset + additionalOffset;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });

                // Close mobile menu after clicking using Bootstrap's collapse
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                }
            }
        });
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Анимация появления элементов при скролле
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.card, .section-title');
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                element.classList.add('animate__animated', 'animate__fadeInUp');
            }
        });
    };

    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Вызываем при загрузке страницы

    // Scroll to top button functionality
    const scrollToTopButton = document.getElementById('scrollToTop');
    
    // Hide button on page load
    scrollToTopButton.style.display = 'none';

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollToTopButton.style.display = 'flex';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });

    scrollToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}); 