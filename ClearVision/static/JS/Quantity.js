function plus_fun() {
    var qty = document.getElementById("qty").value;
    qty++;
    var qty = document.getElementById("qty").value = qty++;
}

function minus_fun() {
    var qty = document.getElementById("qty").value;
    qty--;
    var qty = document.getElementById("qty").value = qty--;
}
