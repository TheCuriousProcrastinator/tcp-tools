const downloadLinks = document.querySelectorAll('a[download]');

downloadLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    if (link.dataset.ready === 'true') {
      return;
    }

    event.preventDefault();
    const toolName = link.closest('.tool-card')?.querySelector('h3')?.textContent || 'This tool';
    alert(`${toolName} is almost ready. The download file will be connected here.`);
  });
});
