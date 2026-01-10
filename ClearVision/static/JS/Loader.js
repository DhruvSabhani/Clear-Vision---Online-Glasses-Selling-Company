var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 300);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}

function heart_click() {
  document.getElementById("heart").style.color = "red";
  // document.getElementById("wishlist").style.color = "red";
}