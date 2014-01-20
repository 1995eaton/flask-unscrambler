$(document).ready(function() {
	document.form.inputAnagrams.focus();
	$('.githubLogo').click( function() {
		window.location='https://github.com/1995eaton/flask-unscrambler';
	});
	$(".listAnagrams").animate({'top': '+=30'}, 200);
	$("#infoButton").click(function() {
		$("#infoButton").animate({"right": "-=25"}, 500);
		$("#infoBox").animate({'right': '+=192'}, 500);
	});
	$('.closeBox,.inputBox').click(function() {
      if ($("#infoBox").position().left != window.innerWidth) {
         $("#infoButton").animate({"right": "+=25"}, 500);
         $("#infoBox").animate({"right": "-=192"}, 500);
      }
	});
});
