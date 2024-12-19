// static/js/custom_map.js
document.addEventListener('DOMContentLoaded', function () {
    function init() {
        var myMap = new ymaps.Map("map", {
            center: [55.76, 37.64],
            zoom: 10
        });

        myMap.events.add('click', function (e) {
            var coords = e.get('coords');
            document.getElementById('id_latitude').value = coords[0];
            document.getElementById('id_longitude').value = coords[1];
        });
    }

    ymaps.ready(init);
});
