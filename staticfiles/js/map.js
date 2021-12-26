var roundLatLng = Formatters.roundLatLng;
var center = [4.890659, 52.373154];
var popup = new tt.Popup({
    offset: 35
});
var map = tt.map({
    key: '<your-tomtom-maps-API-key>',
    container: 'map',
    dragPan: !isMobileOrTablet(),
    center: center,
    zoom: 14
});
map.addControl(new tt.FullscreenControl());
map.addControl(new tt.NavigationControl());
var marker = new tt.Marker({
    draggable: true
}).setLngLat(center).addTo(map);
function onDragEnd() {
    var lngLat = marker.getLngLat();
    lngLat = new tt.LngLat(roundLatLng(lngLat.lng), roundLatLng(lngLat.lat));
    popup.setHTML(lngLat.toString());
    popup.setLngLat(lngLat);
    marker.setPopup(popup);
    marker.togglePopup();
}
marker.on('dragend', onDragEnd);