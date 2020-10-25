
function get_request() {
    var xhttp = new XMLHttpRequest();

    xhttp.open("GET", "/hello", true);
    xhttp.onreadystatechange = function() {
        if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
        // Typical action to be performed when the document is ready:
            data = JSON.parse(xhttp.responseText);
            document.getElementById("demo").innerHTML = xhttp.responseText;
        }
    };
    xhttp.send();
}


// function post_request(data) {
//     var xhttp = new XMLHttpRequest();
//     xhttp.open("POST", "/test", true);
//     xhttp.setRequestHeader('Content-Type', 'multipart/form-data; charset=utf-8');
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//            // Typical action to be performed when the document is ready:
//         };
//     };
//     xhttp.send(data);
// };
get_request()
