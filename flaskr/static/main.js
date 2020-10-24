var phone = {
    'name': 'iphone',
    'age': 5
};
var jsonString = JSON.stringify(phone);

var xhttp = new XMLHttpRequest();

xhttp.open("GET", "/hello", true);
xhttp.onreadystatechange = function() {
    if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
       // Typical action to be performed when the document is ready:
        data = JSON.parse(xhttp.responseText);
        document.getElementById("demo").innerHTML = xhttp.responseText;
        post_request();
    }
};
xhttp.send();

function post_request() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/hello", true);
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           console.log(xhttp.responseText)
        };
    };
    xhttp.send(jsonString);
};
