$(document).ready(function() {
  var pathname = window.location.pathname; // Returns path only

  if (pathname == "/en/blog/" || pathname == "/en/media/") {
    
    $("#btnSearch").show(0);
  }

  $(".button").click(function() {
    window.location = $(this)
      .find("a")
      .attr("href");
    return false;
  });

  $("#btnSearch").click(function() {
    $(".asheader").fadeToggle(0);
  });

  $("#target").submit(function(event) {
    event.preventDefault();
    toast();
    setTimeout(function(){

       
        event.currentTarget.submit();
    },1500);
    
   
  });
});

function toast() {
  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(function() {
    x.className = x.className.replace("show", "");
  }, 3000);
}
