
// // function get_request() {
// //     var xhttp = new XMLHttpRequest();

// //     xhttp.open("GET", "/hello", true);
// //     xhttp.onreadystatechange = function() {
// //         if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
// //         // Typical action to be performed when the document is ready:
// //             data = JSON.parse(xhttp.responseText);
// //             document.getElementById("demo").innerHTML = xhttp.responseText;
// //         }
// //     };
// //     xhttp.send();
// // }


// // // function post_request(data) {
// // //     var xhttp = new XMLHttpRequest();
// // //     xhttp.open("POST", "/test", true);
// // //     xhttp.setRequestHeader('Content-Type', 'multipart/form-data; charset=utf-8');
// // //     xhttp.onreadystatechange = function() {
// // //         if (this.readyState == 4 && this.status == 200) {
// // //            // Typical action to be performed when the document is ready:
// // //         };
// // //     };
// // //     xhttp.send(data);
// // // };
// // get_request()

// async function onload_function() {
//     return new Promise(function (resolve) {
//         let requestURL = 'http://localhost:5000/json';
//         let request = new XMLHttpRequest();
//         request.open('GET', requestURL, true);
//         request.send();
//         request.onload = function () {
//             var addresses = JSON.parse(request.responseText);
//             console.log(addresses)
//             var markers = new Array;
//             var addresses_only = new Array;
//             // Sort the list of addresses //
//             for (var i = 0; i < addresses.length+1; i++) {
//                 if(!(i == addresses.length)) {
//                     addresses_only.push(addresses[i]['address'])
//                 } else {
//                     addresses_only.sort();
//                     console.log(addresses_only)
//                     var list = [addresses, markers, addresses_only]
//                     resolve(list);
//                 }
//             }
//         };
//     });
// };
// function initMap() {
    
//     function CustomMarker(latlng, map, imageSrc) { 
//         this.latlng_ = latlng;
//         this.imageSrc = imageSrc; //added imageSrc
//         this.setMap(map);
//     }

//     CustomMarker.prototype = new google.maps.OverlayView();

//     CustomMarker.prototype.draw = function () {
//         // Check if the div has been created.
//         var div = this.div_;
//         if (!div) {
//             // Create a overlay text DIV
//             div = this.div_ = document.createElement('div');
//             // Create the DIV representing our CustomMarker
//             div.className = "customMarker" //replaced styles with className
//             var img = document.createElement("img");
//             img.src = this.imageSrc; //attach passed image uri
//             div.appendChild(img);

//             // Then add the overlay to the DOM
//             var panes = this.getPanes();
//             panes.overlayImage.appendChild(div);
//             window.add_listener(div);

//         }
//         // Position the overlay 
//         var point = this.getProjection().fromLatLngToDivPixel(this.latlng_);
//         if (point) {
//             div.style.left = point.x + 'px';
//             div.style.top = point.y + 'px';
//         }
//     };

//     CustomMarker.prototype.remove = function () {
//         // Check if the overlay was on the map and needs to be removed.
//         if (this.div_) {
//             this.div_.parentNode.removeChild(this.div_);
//             this.div_ = null;
//         }
//     };

//     CustomMarker.prototype.getPosition = function () {
//         return this.latlng_;
//     };
      
//     //   document.getElementById('entry_list_div').style.height = `${window.innerHeight}px`;
//     //   document.getElementById('entry-map').style.display = 'none';
//       var center = {lat: 0, lng: 0};
//       var map = new google.maps.Map(
//           document.getElementById("entry-map"), {zoom: 1, center: center});
//       var geocoder = new google.maps.Geocoder();
//       geocodeAddress(geocoder, map, CustomMarker);
// };



// async function geocodeAddress(geocoder, resultsMap, CustomMarker) {
//     list = await onload_function();
//     addresses = list[0];
//     markers = list[1];
//     window.resultslist = new Array;
//     window.count = 0;
//     for (var i=0; i < addresses.length+1; i++) {
//         if (i != addresses.length) {
//             marker = await processAddress(geocoder, resultsMap, i, addresses, CustomMarker);
//             if (marker != 'null') {
//                 markers.push(marker);
//             };
//         } else {
//             compute(resultsMap);
//         };
//     };
// };


// async function processAddress(geocoder, resultsMap, i, addresses, CustomMarker) {
//     return new Promise(function (resolve) {
//         geocoder.geocode({'address': addresses[i]['address']}, function(results, status) {
//           if (status === 'OK') {
//             resultslist.push(results[0])
//             var marker = new CustomMarker(
//                 new google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng()),
//                 resultsMap,
//                 addresses[i]['profile_pic']
//             )
//                 window.add_listener = function(div) {
//                     var local_count = window.count;
//                     google.maps.event.addDomListener(div, "click", function (event) {
//                         resultsMap.setZoom(15);
//                         console.log(resultslist, local_count)
//                         resultsMap.setCenter(resultslist[local_count].geometry.location);
//                         div = document.getElementById(`${i+1}`);
//                         // document.getElementById('entry-list-div').style.backgroundColor = 'white';
//                         div.style.backgroundColor = 'orange';
//                     });
//                     window.count+=1;
//                 }
//             var div = document.getElementById(`${i+1}`);
//             div.addEventListener('click', function () {
//                     resultsMap.setZoom(15);
//                     // resultsMap.setCenter(results[0].geometry.location)
//                     div.style.backgroundColor = 'orange';
//                     console.log(div)
//                 });
//             ///////// ADD LISTENERS /////////
//             resolve(marker);
//             // console.log(markers);
//             // formatted_string = results[0].formatted_address.split(',')[0]
//             // for (i=0, i < addresses.length; i++) {

//             // }
//           } else {
//             resolve('null')
//           };
//         });
//     });
// };

// function compute(map) {
//     //SETTING HEIGHT OF ENTRY LIST DIV //
//     var total_lat_list = new Array;
//     var total_lng_list = new Array;
//     var total_lat = 0;
//     var total_lng = 0;
//     var i = 0;
//     for (i=0; i < markers.length; i++) {
//         if (!(total_lat_list.includes(markers[i].getPosition().lat()))) {
//             total_lat_list.push(markers[i].getPosition().lat());
//             total_lat += markers[i].getPosition().lat();
        
//         }
//         if (!(total_lng_list.includes(markers[i].getPosition().lng()))) { 
//             total_lng += markers[i].getPosition().lng();
//             total_lng_list.push(markers[i].getPosition().lng());
//         }
//     };

//     // total_lat = total_lat / total_lat_list.length;
//     // total_lng = total_lng / total_lng_list.length;
//     // //37.6483355 -121.908439//
//     // map.setCenter({lat: total_lat, lng: total_lng});
//     // MAXIMUM LAT IN BETWEEN TWO POINTS //
//     biggest_lat = Math.abs(Math.min(...total_lat_list) - Math.max(...total_lat_list));
//     biggest_lng = Math.abs(Math.min(...total_lng_list) - Math.max(...total_lng_list));
//     //MULTIPLYING BY 100 for more precision //
//     small_lat = Math.min(...total_lat_list)
//     small_lng = Math.min(...total_lng_list)
//     average_lat = (biggest_lat/2)+small_lat
//     average_lng = (biggest_lng/2)+small_lng
//     map.setCenter({lat:average_lat, lng:average_lng})

//     biggest_lat = biggest_lat*100;
//     biggest_lng = biggest_lng*100;
//     // console.log('biggest lat: ', biggest_lat, 'biggest lng :', biggest_lng)
//     // WIDTH OF MAP: CALLING LOADING_DIV SINCE ENTRY-MAP's display is none //
//     width_of_div = document.getElementById('loading-container').offsetWidth;
//     height_of_div = document.getElementById('loading-container').offsetHeight;
//     // MULTIPLY THIS BY 2^ZOOM to get the ratio //
//     // console.log(width_of_div, height_of_div)
//     const zoom_constant = 0.00712402343;
//     width_ratio = width_of_div / biggest_lng;
//     height_ratio = height_of_div / biggest_lat;
//     // console.log('width_ratio: ', width_ratio, 'height_ratio :', height_ratio);
//     zoom_level_height = Math.log(height_ratio / zoom_constant) / Math.log(2);
//     zoom_level_width = Math.log(width_ratio / zoom_constant) / Math.log(2);
//     // console.log(zoom_level_height, zoom_level_width);
//     var zoom_level = Math.min(zoom_level_height, zoom_level_width);
//     zoom_level -= 1;
//     console.log(zoom_level);
//     map.setZoom(zoom_level);
//     document.getElementById('loading').style.display = 'none';
//     document.getElementById('entry-map').style.display = 'block';
// };
let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("entry-map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}


