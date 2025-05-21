document.addEventListener('DOMContentLoaded', function () {
  const tabs = document.querySelectorAll('.tab-links li');
  const contents = document.querySelectorAll('.tab');

  tabs.forEach(tab => {
    tab.addEventListener('click', function (e) {
      e.preventDefault();
      tabs.forEach(t => t.classList.remove('active'));
      contents.forEach(c => c.classList.remove('active'));

      tab.classList.add('active');
      const target = document.querySelector(tab.querySelector('a').getAttribute('href'));
      if (target) target.classList.add('active');
    });
  });
});
