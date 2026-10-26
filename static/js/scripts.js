// Mobile menu toggle. Replaces the jQuery + Bootstrap JS bundle the theme used
// to load from CDNs; nothing else on the site needed them.
(function () {
    var button = document.querySelector('#sideNav .navbar-toggler');
    var menu = document.getElementById('siteNav');
    if (!button || !menu) return;

    button.addEventListener('click', function () {
        var open = menu.classList.toggle('show');
        button.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
})();
