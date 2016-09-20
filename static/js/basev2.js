function myFunction() {
    var x = document.getElementById("nav-collapse");
    if (x.className === "nav-collapse") {
        x.className += " responsive";
    } else {
        x.className = "nav-collapse";
    }
}