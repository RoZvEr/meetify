var myNav = $("header");

$(window).on('scroll', function() {
  "use strict";
  if ($(window).scrollTop() >= 200) {
    myNav.addClass("scroll");
  } else {
    myNav.removeClass("scroll");
  }
});