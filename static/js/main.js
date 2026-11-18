/**
 * Chelamsetty Chaitanya - Editorial Portfolio Interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Animate skill progress bars on scroll
  const skillBars = document.querySelectorAll('.skill-fill');
  
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const targetWidth = entry.target.style.width;
          entry.target.style.width = '0%';
          setTimeout(() => {
            entry.target.style.width = targetWidth;
          }, 100);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    skillBars.forEach(bar => observer.observe(bar));
  }

  // 2. Click to copy contact values with subtle notification
  const contactValues = document.querySelectorAll('.contact-value');
  contactValues.forEach(elem => {
    elem.addEventListener('click', (e) => {
      const text = elem.innerText.trim();
      if (text.includes('@') || text.includes('+91')) {
        navigator.clipboard.writeText(text).then(() => {
          const original = elem.innerText;
          elem.innerText = 'Copied to clipboard!';
          setTimeout(() => {
            elem.innerText = original;
          }, 1800);
        }).catch(() => {});
      }
    });
  });

  // 3. Stamp Badge click interaction
  const rotatingBadge = document.querySelector('.rotating-badge-wrapper');
  if (rotatingBadge) {
    let fast = false;
    rotatingBadge.addEventListener('click', () => {
      const inner = rotatingBadge.querySelector('.badge-inner-spin');
      if (inner) {
        fast = !fast;
        inner.style.animationDuration = fast ? '6s' : '22s';
      }
    });
  }

  console.log('Chelamsetty Chaitanya Editorial Portfolio Loaded Successfully.');
});
