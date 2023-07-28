const closeMarkerPopup = document.getElementById('closeMarkerPopup');

// Creating map options
let mapOptions = {
  center: [54.989346, 73.368203],
  zoom: 12,
  scrollWheelZoom: true,
};
// Creating a map object
let map = new L.map('map', mapOptions);

// Creating a Layer object
let layer = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Adding layer to the map
map.addLayer(layer);

let markerIcon = L.icon({
  iconUrl: '../static/img/marker.svg',
  iconSize: [38, 95],
});

if (document.getElementById('1')) {
  const markerPopup = document.getElementById('1');
  let marker1 = L.marker([54.950474, 73.389700], {icon: markerIcon});
  marker1.addTo(map);
  function closeMarker1(e) {
    markerPopup.classList.add('popup__active');
  }
  function showMarker1() {
    markerPopup.classList.remove('popup__active');
  }
  marker1.on("click", closeMarker1);
  closeMarkerPopup.onclick = showMarker1;
}

if (document.getElementById('2')) {
  const markerPopup = document.getElementById('2');
  let marker2 = L.marker([54.985395, 73.387463], {icon: markerIcon});
  marker2.addTo(map);
  function closeMarker2(e) {
    markerPopup.classList.add('popup__active');
  }
  function showMarker2() {
    markerPopup.classList.remove('popup__active');
  }
  marker2.on("click", closeMarker2);
  closeMarkerPopup.onclick = showMarker2;
}

if (document.getElementById('3')) {
  const markerPopup = document.getElementById('3');
  let marker3 = L.marker([54.994971, 73.356381], {icon: markerIcon});
  marker3.addTo(map);
  function closeMarker3(e) {
    markerPopup.classList.add('popup__active');
  }
  function showMarker3() {
    markerPopup.classList.remove('popup__active');
  }
  marker3.on("click", closeMarker3);
  closeMarkerPopup.onclick = showMarker3;
}

if (document.getElementById('4')) {
  const markerPopup = document.getElementById('4');
  let marker4 = L.marker([54.985395, 73.387463], {icon: markerIcon});
  marker4.addTo(map);
  function closeMarker4(e) {
    markerPopup.classList.add('popup__active');
  }
  function showMarker4() {
    markerPopup.classList.remove('popup__active');
  }
  marker4.on("click", closeMarker4);
  closeMarkerPopup.onclick = showMarker4;
}

if (document.getElementById('5')) {
  const markerPopup = document.getElementById('5');
  let marker5 = L.marker([54.978565, 73.374743], {icon: markerIcon});
  marker5.addTo(map);
  function closeMarker5(e) {
    markerPopup.classList.add('popup__active');
  }
  function showMarker5() {
    markerPopup.classList.remove('popup__active');
  }
  marker5.on("click", closeMarker5);
  closeMarkerPopup.onclick = showMarker5;
}


// let marker1 = L.marker([54.950474, 73.389700], {icon: markerIcon});
// let marker2 = L.marker([54.985395, 73.387463], {icon: markerIcon});
// let marker3 = L.marker([54.994971, 73.356381], {icon: markerIcon});
// let marker4 = L.marker([54.951953, 73.398261], {icon: markerIcon});
// let marker5 = L.marker([54.978565, 73.374743], {icon: markerIcon});




