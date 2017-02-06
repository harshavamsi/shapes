$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
$('#contact').on('submit', function(event){
    event.preventDefault();
    contact();
});
function contact() {
	$("#send").text("Sending..");
    $.ajax({
        url : "contact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#name').val(), phone : $('#phone').val(), email : $('#email').val(), message : $('#message').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#name').val('');
            $('#phone').val('')
            $('#email').val('')
            $('#message').val('')
             // remove the value from the input
             console.log("suxes")
             $('#success').text("Thanks for contacting us. We'll get back to you soon!");
             $("#send").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$('#dancecontact').on('submit', function(event){
    event.preventDefault();
    dancecontact();
});
function dancecontact() {
    $("#dancesend").text("Sending..");
    console.log($('#dancemessage').val());
    $.ajax({
        url : "/dancecontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#dancename').val(), phone : $('#dancephone').val(), email : $('#danceemail').val(), message : $('#dancemessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#dancename').val('');
            $('#dancephone').val('')
            $('#danceemail').val('')
            $('#dancemessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#dancesuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#dancesend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$('#musiccontact').on('submit', function(event){
    event.preventDefault();
    musiccontact();
});
function musiccontact() {
    $("#musicsend").text("Sending..");
    $.ajax({
        url : "/musiccontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#musicname').val(), phone : $('#musicphone').val(), email : $('#musicemail').val(), message : $('#musicmessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#musicname').val('');
            $('#musicphone').val('')
            $('#musicemail').val('')
            $('#musicmessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#musicsuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#musicsend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$('#quizcontact').on('submit', function(event){
    event.preventDefault();
    quizcontact();
});
function quizcontact() {
    $("#quizsend").text("Sending..");
    $.ajax({
        url : "/quizcontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#quizname').val(), phone : $('#quizphone').val(), email : $('#quizemail').val(), message : $('#quizmessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#quizname').val('');
            $('#quizphone').val('')
            $('#quizemail').val('')
            $('#quizmessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#quizsuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#quizsend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$('#theatrecontact').on('submit', function(event){
    event.preventDefault();
    theatrecontact();
});
function theatrecontact() {
    $("#theatresend").text("Sending..");
    $.ajax({
        url : "/theatrecontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#theatrename').val(), phone : $('#theatrephone').val(), email : $('#theatreemail').val(), message : $('#theatremessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#theatrename').val('');
            $('#theatrephone').val('')
            $('#theatreemail').val('')
            $('#theatremessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#theatresuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#theatresend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$('#acmcontact').on('submit', function(event){
    event.preventDefault();
    acmcontact();
});
function acmcontact() {
    $("#acmsend").text("Sending..");
    $.ajax({
        url : "/acmcontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#acmname').val(), phone : $('#acmphone').val(), email : $('#acmemail').val(), message : $('#acmmessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#acmname').val('');
            $('#acmphone').val('')
            $('#acmemail').val('')
            $('#acmmessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#acmsuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#acmsend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$('#ieeecontact').on('submit', function(event){
    event.preventDefault();
    ieeecontact();
});
function ieeecontact() {
    $("#ieeesend").text("Sending..");
    $.ajax({
        url : "/ieeecontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#ieeename').val(), phone : $('#ieeephone').val(), email : $('#ieeeemail').val(), message : $('#ieeemessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#ieeename').val('');
            $('#ieeephone').val('')
            $('#ieeeemail').val('')
            $('#ieeemessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#ieeesuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#ieeesend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


$('#enigmacontact').on('submit', function(event){
    event.preventDefault();
    enigmacontact();
});
function enigmacontact() {
    $("#enigmasend").text("Sending..");
    $.ajax({
        url : "/enigmacontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#enigmaname').val(), phone : $('#enigmaphone').val(), email : $('#enigmaemail').val(), message : $('#enigmamessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#enigmaname').val('');
            $('#enigmaphone').val('')
            $('#enigmaemail').val('')
            $('#enigmamessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#enigmasuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#enigmasend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


$('#avionscontact').on('submit', function(event){
    event.preventDefault();
    avionscontact();
});
function ieeecontact() {
    $("#avionssend").text("Sending..");
    $.ajax({
        url : "/avionscontact/", // the endpoint
        type : "POST", // http method
        data : { name : $('#ieeename').val(), phone : $('#ieeephone').val(), email : $('#ieeeemail').val(), message : $('#ieeemessage').val() }, // data sent with the post request
        
        // handle a successful response
        success : function(json) {
            $('#avionsname').val('');
            $('#avionsphone').val('')
            $('#avionsemail').val('')
            $('#avionsmessage').val('')
             // remove the value from the input
             console.log("suxes")
             $('#avionssuccess').text("Thanks for contacting us. We'll get back to you soon!");
             $("#avionssend").text("Send");
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$(document).ready(function(e) {
	$('.with-hover-text, .regular-link').click(function(e){
		e.stopPropagation();
	});
	
	/***************
	* = Hover text *
	* Hover text for the last slide
	***************/
	$('.with-hover-text').hover(
		function(e) {
			$(this).css('overflow', 'visible');
			$(this).find('.hover-text')
				.show()
				.css('opacity', 0)
				.delay(200)
				.animate(
					{
						paddingTop: '25px',
						opacity: 1
					},
					'fast',
					'linear'
				);
		},
		function(e) {
			var obj = $(this);
			$(this).find('.hover-text')
				.animate(
					{
						paddingTop: '0',
						opacity: 0
					},
					'fast',
					'linear',
					function() {
						$(this).hide();
						$( obj ).css('overflow', 'hidden');
					}
				);
		}
	);
	
	var img_loaded = 0;
	var j_images = [];
	
	/*************************
	* = Controls active menu *
	* Hover text for the last slide
	*************************/
	$('#slide-3 img').each(function(index, element) {
		var time = new Date().getTime();
		var oldHref = $(this).attr('src');
		var myImg = $('<img />').attr('src', oldHref + '?' + time );
		
		myImg.load(function(e) {
			img_loaded += 1;;
			if ( img_loaded == $('#slide-3 img').length ) {
				$(function() {
					var pause = 10;
					$(document).scroll(function(e) {
						delay(function() {
							
							var tops = [];
							
							$('.story').each(function(index, element) {
								tops.push( $(element).offset().top - 200 );
							});
				
							var scroll_top = $(this).scrollTop();
							
							var lis = $('.nav > li');
							
							for ( var i=tops.length-1; i>=0; i-- ) {
								if ( scroll_top >= tops[i] ) {
									menu_focus( lis[i], i+1 );
									break;
								}
							}
						},
						pause);
					});
					$(document).scroll();
				});
			}
		});
	});
	
});

/******************
* = Gallery width *
******************/
$(function() {
	var pause = 50; // will only process code within delay(function() { ... }) every 100ms.
	$(window).resize(function() {
		delay(function() {
				var gallery_images = $('#slide-3 img');
				
				var images_per_row = 0;
				if ( gallery_images.length % 2 == 0 ) {
					images_per_row = gallery_images.length / 2;
				} else {
					images_per_row = gallery_images.length / 2 + 1;
				}
				
				var gallery_width = $('#slide-3 img').width() * $('#slide-3 img').length;
				gallery_width /= 2;
				if ( $('#slide-3 img').length % 2 != 0 ) {
					gallery_width += $('#slide-3 img').width();
				}
				
				$('#slide-3 .row').css('width', gallery_width );
				
				var left_pos = $('#slide-3 .row').width() - $('body').width();
				left_pos /= -2;
				
				$('#slide-3 .row').css('left', left_pos);
			
			},
			pause
		);
	});
	$(window).resize();
});

var delay = (function(){
	var timer = 0;
	return function(callback, ms){
		clearTimeout (timer);
		timer = setTimeout(callback, ms);
	};
})();

function menu_focus( element, i ) {
	if ( $(element).hasClass('active') ) {
		if ( i == 6 ) {
			if ( $('.navbar').hasClass('inv') == false )
				return;
		} else {
			return;
		}
	}
	
	
		
	if ( i == 1 || i == 6 )
		$('.navbar').removeClass('inv');
	else
		$('.navbar').addClass('inv');
	
	$('.nav > li').removeClass('active');
	$(element).addClass('active');
	
	var icon = $(element).find('.icon');
	
	var left_pos = icon.offset().left - $('.nav').offset().left;
	var el_width = icon.width() + $(element).find('.text').width() + 10;
	
	$('.active-menu').stop(false, false).animate(
		{
			left: left_pos,
			width: el_width
		},
		1500,
		'easeInOutQuart'
	);
}

function enable_arrows( dataslide ) {


}

/*************
* = Parallax *
*************/
jQuery(document).ready(function ($) {
	//Cache some variables
	var links = $('.nav').find('li');
	slide = $('.slide');
	button = $('.button');
	mywindow = $(window);
	htmlbody = $('html,body');
	
	//Create a function that will be passed a slide number and then will scroll to that slide using jquerys animate. The Jquery
	//easing plugin is also used, so we passed in the easing method of 'easeInOutQuint' which is available throught the plugin.
	function goToByScroll(dataslide) {
		var offset_top = ( dataslide == 1 ) ? '0px' : $('.slide[data-slide="' + dataslide + '"]').offset().top;
		
		htmlbody.stop(false, false).animate({
			scrollTop: offset_top
		}, 1500, 'easeInOutQuart');
	}
	
	//When the user clicks on the navigation links, get the data-slide attribute value of the link and pass that variable to the goToByScroll function
	links.click(function (e) {
		
		dataslide = $(this).attr('data-slide');
		goToByScroll(dataslide);
		$(".nav-collapse").collapse('hide');
	});
	
	//When the user clicks on the navigation links, get the data-slide attribute value of the link and pass that variable to the goToByScroll function
	$('.navigation-slide').click(function (e) {
		e.preventDefault();
		dataslide = $(this).attr('data-slide');
		goToByScroll(dataslide);
		$(".nav-collapse").collapse('hide');
	});
});

/***************
* = Menu hover *
***************/
jQuery(document).ready(function ($) {
	//Cache some variables
	var menu_item = $('.nav').find('li');
	
	menu_item.hover(
		function(e) {
			var icon = $(this).find('.icon');
			
			var left_pos = icon.offset().left - $('.nav').offset().left;
			var el_width = icon.width() + $(this).find('.text').width() + 10;
			
			var hover_bar = $('<div class="active-menu special-active-menu"></div>')
				.css('left', left_pos)
				.css('width', el_width)
				.attr('id', 'special-active-menu-' + $(this).data('slide') );
			
			$('.active-menu').after( hover_bar );
		},
		function(e) {
			$('.special-active-menu').remove();
		}
	);
});

/******************
* = Gallery hover *
******************/
jQuery(document).ready(function ($) {
	//Cache some variables
	var images = $('#slide-3 a');
	
	images.hover(
		function(e) {
			var asta = $(this).find('img');
			$('#slide-3 img').not( asta ).stop(false, false).animate(
				{
					opacity: .5
				},
				'fast',
				'linear'
			);
			var zoom = $('<div class="zoom"></div>');
			if ( $(this).hasClass('video') ) {
				zoom.addClass('video');
			}
			$(this).prepend(zoom);
		},
		function(e) {
			$('#slide-3 img').stop(false, false).animate(
				{
					opacity: 1
				},
				'fast',
				'linear'
			);
			$('.zoom').remove();
		}
	);
});
$("#arrow-left").click(function(){
    window.location.href = "/";
});
/******************
* = Arrows click  *
******************/
jQuery(document).ready(function ($) {
	//Cache some variables
	var arrows = $('#arrows div');
	
	arrows.click(function(e) {
		e.preventDefault();
		
		if ( $(this).hasClass('disabled') )
			return;
		
		var slide = null;
		var datasheet = $('.nav > li.active').data('slide');
		var offset_top = false;
		var offset_left = false;
		
		
		switch( $(this).attr('id') ) {
			case 'arrow-up':
				offset_top = ( datasheet - 1 == 1 ) ? '0px' : $('.slide[data-slide="' + (datasheet-1) + '"]').offset().top;
				break;
			case 'arrow-down':
				offset_top = $('.slide[data-slide="' + (datasheet+1) + '"]').offset().top;
				break;
			case 'arrow-left':
				offset_left = $('#slide-3 .row').offset().left + 452;
				if ( offset_left > 0 ) {
					offset_left = '0px';
				}
				break;
			case 'arrow-right':
				offset_left = $('#slide-3 .row').offset().left - 452;
				if ( offset_left < $('body').width() - $('#slide-3 .row').width() ) {
					offset_left = $('body').width() - $('#slide-3 .row').width();
				}
				break;
		}
		
		if ( offset_top != false ) {
			htmlbody.stop(false, false).animate({
				scrollTop: offset_top
			}, 1500, 'easeInOutQuart');
		}
		
		if ( offset_left != false ) {
			if ( $('#slide-3 .row').width() != $('body').width() ) {
				$('#slide-3 .row').stop(false, false).animate({
					left: offset_left
				}, 1500, 'easeInOutQuart');
			}
		}
	});
});