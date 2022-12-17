
let navMenuBtn = document.querySelector(".navigation .top button");
let menuOpened = false;
let text = document.querySelectorAll(".navbtn span");
let menu = document.querySelector('.bottom');
function openClose(){
    if(menuOpened == false){
        menu.style.width = '20rem';
        menuOpened=true;
        for (var i = 0; i < text.length; i++) {
          text[i].style.width = "100px";
          text[i].style.height = '10px';
          text[i].style.display = 'inline-block';
        }
    }
    else if(menuOpened == true){
        menu.style.width = '3.4rem';
        menuOpened =false;
        for (var i = 0; i < text.length; i++) {
            text[i].style.display= 'none'; 
            text[i].style.width = "0";
            text[i].style.height = '0'; 
        }
    }
}
