function header_show() {
    document.getElementById("firstbars").style.display = "none";

    document.getElementById("secondbars").style.display = "flex";

    document.getElementById("headerfirstblock").style.display = "none";

    document.getElementById("headersecondblock").style.transition = ".3s";
    document.getElementById("headersecondblock").style.width = "";
    document.getElementById("headersecondblock").style.left = "-5px";

    document.getElementById("loader").style.left = "55%";

    document.getElementById("add").style.left = "50%";
    document.getElementById("add").style.transition = ".3s";
};

function header_hide() {
    document.getElementById("firstbars").style.display = "flex";

    document.getElementById("secondbars").style.display = "none";

    document.getElementById("headerfirstblock").style.display = "flex";

    document.getElementById("headersecondblock").style.transition = ".3s";
    document.getElementById("headersecondblock").style.width = "76vw";
    document.getElementById("headersecondblock").style.left = "322px";

    document.getElementById("loader").style.left = "65%";

    document.getElementById("add").style.left = "60%";
    document.getElementById("add").style.transition = ".3s";
}

function show_table() {
    document.getElementById("add_goggles_form").style.display = "none";
}

function numberWithCommas(x) {
    x = x.toString();
    var pattern = /(-?\d+)(\d{3})/;
    while (pattern.test(x))
        x = x.replace(pattern, "$1,$2");
    return x;
}

function down_details() {
    document.getElementById("couponsimg").style.display = "block";
    document.getElementById("show_down").style.display = "none";
    document.getElementById("show_up").style.display = "block";
}

function up_details() {
    document.getElementById("couponsimg").style.display = "none";
    document.getElementById("show_down").style.display = "block";
    document.getElementById("show_up").style.display = "none";
}
