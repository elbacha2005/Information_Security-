(function () {

    // Check if analytics cookie exists on THIS publisher's domain
    function getCookie(name) {
        let match = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
        return match ? match[1] : null;
    }

    let uid = getCookie("_analytics_id");

    // If no cookie, generate a random ID and store it
    if (!uid) {
        uid = Math.random().toString(36).substring(2, 18);
        document.cookie = "_analytics_id=" + uid + "; max-age=31536000; path=/";
    }

    // Send tracking data to the analytics server
    let data = {
        uid: uid,
        url: window.location.href,
        title: document.title,
        referrer: document.referrer,
        timestamp: new Date().toISOString()
    };

    // Send as a query string via an image pixel (common technique)
    let img = new Image();
    img.src = "http://analytics.loc:9100/collect?" + new URLSearchParams(data).toString();
})();