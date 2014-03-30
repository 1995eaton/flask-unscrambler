var input, wordBox, infoBox;

Object.prototype.slideDown = function(start, end, duration) {
  var i = 0;
  var delta = Math.abs(end - start);
  var offset = 0;
  var direction = start < end ? 1 : -1;
  end *= direction;
  function loop() {
    offset = start + direction * delta * Math.sin(i / duration * (Math.PI / 2));
    wordBox.style.top = start + offset + "px";
    if (direction * offset < end) {
      requestAnimationFrame(loop);
    }
    i++;
  }
  loop();
};

function send() {
  if (input.value.trim().length > 1) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", document.URL + "unscramble");
    var formData = new FormData();
    formData.append("letters", input.value);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        if (xhr.responseText.trim() !== "") {
          wordBox.style.top = "0px";
          wordBox.innerHTML = xhr.responseText + "<br>" + wordBox.innerHTML;
          wordBox.slideDown(-12, 12, 20);
        }
      }
    }
    xhr.send(formData);
  }
  input.value = "";
}

var info = {
  mousedown: function() {
    infoBox.main.style.right = "0";
    infoBox.open.style.right = "-50px";
  },
  touchend: function() {
    this.mousedown();
  }
};

var close = {
  mousedown: function() {
    infoBox.main.style.right = "-190px";
    infoBox.open.style.right = "0";
  },
  touchend: function() {
    this.mousedown();
  }
};

function InfoBox(main, open, close) {
  this.main  = main;
  this.open  = open;
  this.close = close;
  return this;
}

input = document.getElementById("input");
wordBox = document.getElementById("anagrams");
var isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
if (window.innerWidth > 400) {
  infoBox = new InfoBox(document.getElementById("info-box"), document.getElementById("info-button"), document.getElementById("close-box"));
  infoBox.open.addEventListener("mousedown", info.mousedown);
  infoBox.close.addEventListener("mousedown", close.mousedown);
  if (isMobile) {
    infoBox.open.addEventListener("touchend", info.touchend);
    infoBox.close.addEventListener("touchend", close.touchend);
  }
} else document.getElementById("info-button").style.display = "none";
input.focus();
