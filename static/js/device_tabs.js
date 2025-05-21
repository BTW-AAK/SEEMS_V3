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

function showTab(id) {
    document.querySelectorAll('.tab-content').forEach(div => div.style.display = 'none');
    document.getElementById(id).style.display = 'block';
}
window.addEventListener('DOMContentLoaded', () => {
    const defaultTab = document.querySelector('.tab-content');
    if (defaultTab) defaultTab.style.display = 'block';
});

document.addEventListener("DOMContentLoaded", () => {
    // Tab switching logic
    const tabs = document.querySelectorAll(".tab-links li");
    const contents = document.querySelectorAll(".tab-content .tab");

    tabs.forEach((tab, idx) => {
        tab.addEventListener("click", (e) => {
            e.preventDefault();

            // Remove 'active' class from all tabs and content
            tabs.forEach(t => t.classList.remove("active"));
            contents.forEach(c => c.classList.remove("active"));

            // Add 'active' to current
            tab.classList.add("active");
            contents[idx].classList.add("active");
        });
    });

    // Fetch chart data and render per tab
    fetch('/refresh')
        .then(res => res.json())
        .then(data => {
            data.data.forEach(device => {
                if (device.energy_wh == 0 && device.voltage == 0 && device.current == 0) return;

                const ctx = document.getElementById(`chart-${device.device_id}`);
                if (!ctx) return;

                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['Energy (Wh)', 'Voltage (V)', 'Current (mA)'],
                        datasets: [{
                            label: `${device.device_id}`,
                            data: [
                                device.energy_wh,
                                device.voltage,
                                device.current
                            ],
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)'
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            y: { beginAtZero: true }
                        }
                    }
                });
            });
        });
});
