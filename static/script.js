window.onscroll = function() {myFunction()};

let header = document.getElementById("venue-header");
let sticky = header.offsetTop;

let table = document.getElementById("shows_table")

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    table.classList.add("sticky-table")
  } else {
    header.classList.remove("sticky");
  }
}