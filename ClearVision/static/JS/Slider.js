function left_goggles_type() {
    document.getElementById("goggles_type").scrollLeft -= 100;
};

function right_goggles_type() {
    document.getElementById("goggles_type").scrollLeft += 100;
    document.getElementById("goggles_type").style.transition = "width 2s";
};


function left_goggles() {
    document.getElementById("goggles_eyeglasses").scrollLeft -= 100;
    document.getElementById("goggles_eyeglasses").style.transition = "width 1s";
    document.getElementById("goggles_progressive_lenses").scrollLeft -= 100;
    document.getElementById("goggles_power_sunglasses").scrollLeft -= 100;
    document.getElementById("goggles_screen_glasses").scrollLeft -= 100;
    document.getElementById("goggles_sunglasses").scrollLeft -= 100;
    document.getElementById("goggles_safety_glasses").scrollLeft -= 100;
};

function right_goggles() {
    document.getElementById("goggles_eyeglasses").scrollLeft += 1000;
    document.getElementById("goggles_eyeglasses").style.transition = "width 2s";
    document.getElementById("goggles_progressive_lenses").scrollLeft += 100;
    document.getElementById("goggles_power_sunglasses").scrollLeft += 100;
    document.getElementById("goggles_screen_glasses").scrollLeft += 100;
    document.getElementById("goggles_sunglasses").scrollLeft += 100;
    document.getElementById("goggles_safety_glasses").scrollLeft += 100;
};

function down_details() {
    document.getElementById("details1").style.display = "block";
    document.getElementById("details2").style.display = "block";
    document.getElementById("show_down").style.display = "none";
    document.getElementById("show_up").style.display = "block";
}

function up_details() {
    document.getElementById("details1").style.display = "none";
    document.getElementById("details2").style.display = "none";
    document.getElementById("show_down").style.display = "block";
    document.getElementById("show_up").style.display = "none";
}