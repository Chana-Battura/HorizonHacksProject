var theme = 'light';
function toggle_theme(){
  document.documentElement.classList.add('transition');
  if (theme === 'light'){
    document.documentElement.setAttribute('theme', 'light');
    theme = 'light';
  }else{
    document.documentElement.setAttribute('theme', 'dark');
    theme = 'light';
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
