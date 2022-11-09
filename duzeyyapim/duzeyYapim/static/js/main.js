window.addEventListener('load', () => {
  AOS.init({
    duration: 1000,
    easing: 'ease-in-out',
    once: true,
    mirror: false
  })
});
document.addEventListener("DOMContentLoaded", () => {
    function counter(id, start, end, duration) {
     let obj = document.getElementById(id),
      current = start,
      range = end - start,
      increment = end > start ? 1 : -1,
      step = Math.abs(Math.floor(duration / range)),
      timer = setInterval(() => {
       current += increment;
       obj.textContent = current;
       if (current == end) {
        clearInterval(timer);
       }
      }, step);
    }
    counter("count1", 0, 58, 13000);
    counter("count2", 100, 50, 2500);
    counter("count3", 0, 136, 13000);
   });
   
   $(document).ready(function(){
    $(window).scroll(function(){
        $('nav').toggleClass('scrolled',$(this).scrollTop()>50);
           
   });
});
$(document).ready(function(){

  $("#hakkimizda").click(function(){

    $("#slider").removeClass("active");

	  $("#slider2").addClass("active");//stil2 adlı stilimizi sildik ve stil1 stilimizi boskutu id'li divimize atadık.

	});

  $("#anasayfa").click(function(){

    $("#slider2").removeClass("active");

	  $("#slider").addClass("active animate__animated animate__fadeIn animate__slow");//stil2 adlı stilimizi sildik ve stil1 stilimizi boskutu id'li divimize atadık.

	});

});