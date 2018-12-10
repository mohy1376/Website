$(document).ready(function() {
  // serch icon hide
  var pathname = window.location.pathname; // Returns path only

  if (pathname == "/fa/articles/" || pathname == "/fa/news/") {
    
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


  // send aboutus message
  $("#target").submit(function(event) {
    event.preventDefault();
    toast();
    setTimeout(function(){

       
        event.currentTarget.submit();
    },1500);
    
   
  });

   // hide login form
  $(".btnLog").click(function(){ 
    
    
    $(".logwindow").fadeToggle(200);

  });

  // tooltip

  $(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   

});

//send comment message
$("#commentTarget").submit(function(event) {
  event.preventDefault();
  toast();
  setTimeout(function(){

     
      event.currentTarget.submit();
  },1500);
  
 
});

});
// for toast 
function toast() {
  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(function() {
    x.className = x.className.replace("show", "");
  }, 3000);
}

// for login and sigup form

const loginBtn = document.getElementById('login');
const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode.parentNode;
	Array.from(e.target.parentNode.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			signupBtn.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

signupBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode;
	Array.from(e.target.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			loginBtn.parentNode.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

// for comment's reply
function show_reply_form(event) {
  var $this = $(this);
  var comment_id = $this.data('comment-id');

  $('#id_parent').val(comment_id);
  $('#form-comment').insertAfter($this.closest('.comment'));
};

function cancel_reply_form(event) {
  $('#id_comment').val('');
  $('#id_parent').val('');
  $('#form-comment').appendTo($('#wrap_write_comment'));
}

$.fn.ready(function() {
  $('.comment_reply_link').click(show_reply_form);
  $('#cancel_reply').click(cancel_reply_form);
})