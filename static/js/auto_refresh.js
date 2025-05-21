// static/js/auto_refresh.js

setInterval(() => {
    fetch('/refresh')
        .then(response => response.json())
        .then(data => {
            console.log('Auto-refreshed data:', data);
            location.reload();  // Refresh the page to update charts and cost
        })
        .catch(err => console.error('Auto-refresh error:', err));
}, 60000); // 60000 ms = 1 minute
