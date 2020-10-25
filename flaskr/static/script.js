var theme = 'dark';
function toggle_theme(){
  document.documentElement.classList.add('transition');
  if (theme === 'dark'){
    document.documentElement.setAttribute('theme', 'light');
    theme = 'light';
  }else{
    document.documentElement.setAttribute('theme', 'dark');
    theme = 'dark';
  }
  window.setTimeout(function() {
    document.documentElement.classList.remove('transition');
  }, 350);
}

toggle_theme();

function hide(element){
  element.classList.remove('visible-snackbar');
}
function show(element){
  element.classList.add('visible-snackbar')
}
function message(string){
  $('#message')[0].innerHTML = string;
  show($('#message')[0]);
}
