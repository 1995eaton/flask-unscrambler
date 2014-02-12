var animationSpeed = 300;

$(document).ready(function() {
  document.form.inputAnagrams.focus();
  $('.githubLogo').click( function() {
    window.location='https://github.com/1995eaton/flask-unscrambler';
  });
  $(".listAnagrams").animate({'top': '+=30'}, 200);
  $("#infoButton").click(function() {
    $("#infoButton").animate({"right": "-=25"}, animationSpeed);
    $("#infoBox").animate({'right': '+=192'}, animationSpeed);
  });
  $('.closeBox,.inputBox').click(function() {
    if ($("#infoBox").position().left != window.innerWidth) {
      $("#infoButton").animate({"right": "+=25"}, animationSpeed);
      $("#infoBox").animate({"right": "-=192"}, animationSpeed);
    }
  });
});
