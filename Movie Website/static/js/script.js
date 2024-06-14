
function togglePage() {
    var checkbox = document.getElementById('color_mode');
    var isSeries = checkbox.checked;

    // Store the state in local storage
    localStorage.setItem('pageMode', isSeries ? 'series' : 'movies');

    // Update the toggle switch state in the header if present
    var toggleSwitch = document.querySelector('.btn-color-mode-switch-inner');
    if (toggleSwitch) {
        toggleSwitch.setAttribute('data-on', isSeries ? 'SERIES' : 'MOVIES');
        toggleSwitch.setAttribute('data-off', isSeries ? 'MOVIES' : 'SERIES');
    }

    // Redirect to the appropriate page
    if (isSeries) {
        window.location.href = 'serieso';
    } else {
        window.location.href = 'movieso';
    }
}

// On page load, set the toggle state based on local storage
window.onload = function() {
    var pageMode = localStorage.getItem('pageMode');
    if (pageMode === 'series') {
        document.getElementById('color_mode').checked = true;
    }
};
function changeIframeSource(movieId, domain, mode) {
            const iframe = document.getElementById('movieIframe');
            const newUrl = `https://vidsrc${domain}/embed/${mode}/tt${movieId}`;
            iframe.src = ''; // Set the src attribute to an empty string
            setTimeout(() => { iframe.src = newUrl; }, 100); // Update the iframe src attribute after a short delay
        }