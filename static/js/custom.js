/*
Vizion - Al/ML - Chatbot Responsive HTML5 Template
Author: iqonicthemes.in
Version: 1.0
Design and Developed by: iqonicthemes.in
*/
/*----------------------------------------------
Index Of Script
------------------------------------------------
 1 Page Loader
 2 Back To Top
 3 Swiper
 4 Header
 5 slider slick
 6 Countdown
 7 Owl Carousel
 8 Auto tab
 9 Magnific Popup
10 Wow Animation
11 Contact From
------------------------------------------------
Index Of Script
----------------------------------------------*/

(function($) {

	"use strict";
	$(document).ready(function() {



		/*------------------------
		1 Page Loader
		--------------------------*/
		jQuery("#load").fadeOut();
		jQuery("#loading").delay(0).fadeOut("slow");



		/*------------------------
		2 Back To Top
		--------------------------*/
		$('#back-to-top').fadeOut();
		$(window).on("scroll", function() {
			if ($(this).scrollTop() > 250) {
				$('#back-to-top').fadeIn(1400);
			} else {
				$('#back-to-top').fadeOut(400);
			}
		});
		// scroll body to 0px on click
		$('#top').on('click', function() {
			$('top').tooltip('hide');
			$('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});


 		/*------------------------
      	3 Swiper
        --------------------------*/

        var swiper = new Swiper('.swiper-container', {
            autoplay:true,
            slidesPerView: 1,
      spaceBetween: 30,
          scrollbar: {
            el: '.swiper-scrollbar',
            hide: true,
          },
        });

		/*------------------------
        4 Header
        --------------------------*/
        $('.navbar-nav li a').on('click', function(e) {
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top - 0
            }, 1500);
            e.preventDefault();
        });
        $(window).on('scroll', function() {
            if ($(this).scrollTop() > 100) {
                $('header').addClass('menu-sticky');
            } else {
                $('header').removeClass('menu-sticky');
            }
        });

        /*------------------------
        5 slider slick
        --------------------------*/
		  $('.slider-for').slick({
		  slidesToShow: 1,
		  slidesToScroll: 1,
		  arrows: false,
		  fade: true,
		  asNavFor: '.slider-nav'
		});
		$('.slider-nav').slick({
		  slidesToShow: 8,
		  slidesToScroll: 1,
		  asNavFor: '.slider-for',
		  dots: false,
		  centerMode: true,
		  focusOnSelect: true,
		  responsive: [{
 			breakpoint: 1024,
 			settings: {
 				slidesToShow: 5,
 				slidesToScroll: 5,
 			}
 		}, {
 			breakpoint: 640,
 			settings: {
 				slidesToShow: 4,
 				slidesToScroll: 4,
			}
 		}, {
 			breakpoint: 420,
 			settings: {
 				slidesToShow: 2,
 				slidesToScroll: 2,
		}
 		}]


		});


		/*------------------------
        6 Countdown
        --------------------------*/
        $('#countdown').countdown({
            date: '10/01/2019 23:59:59',
            day: 'Day',
            days: 'Days'
        });



		/*------------------------
		7 Owl Carousel
		--------------------------*/
		$('.owl-carousel').each(function() {
			var $carousel = $(this);
			$carousel.owlCarousel({
				items: $carousel.data("items"),
				loop: $carousel.data("loop"),
				margin: $carousel.data("margin"),
				nav: $carousel.data("nav"),
				dots: $carousel.data("dots"),
				autoplay: $carousel.data("autoplay"),
				autoplayTimeout: $carousel.data("autoplay-timeout"),
				navText: ['<i class="ion-ios-arrow-thin-left"></i>', '<i class="ion-ios-arrow-thin-right"></i>'],
				responsiveClass: true,
				responsive: {
					// breakpoint from 0 up
					0: {
						items: $carousel.data("items-mobile-sm")
					},
					// breakpoint from 480 up
					480: {
						items: $carousel.data("items-mobile")
					},
					// breakpoint from 786 up
					786: {
						items: $carousel.data("items-tab")
					},
					// breakpoint from 1023 up
					1023: {
						items: $carousel.data("items-laptop")
					},
					1199: {
						items: $carousel.data("items")
					}
				}
			});
		});


		/*------------------------
		8 Auto tab
		--------------------------*/

			var HM = {
    //tab
    jqs_slideList: '.slideList',
    jqs_tabList: '.slides .carouselLinks',


    init: function() {
        //init sliders
        var aSliders = $(this.jqs_slideList);
        if (aSliders.length > 0) {
            this.slideShow(aSliders);
        }

        //init the carousels that are lists of links
        // $('.carousel.icons').hellmannsCrsl({
        //     rotateSpeed: 5000,
        //     viewport: '.carouselLinks'
        // });
    },

    slideShow: function(eSlideListParam) {
        var slideList = eSlideListParam,
            slides = slideList.find('li'),
            tabList = slideList.siblings('.carouselLinks'),
            tabs = tabList.find('.object-new'),
            speed = 500;


        tabs.on('click', 'a', function(e) {
            $(this).trigger('slides.swap');
            e.preventDefault();
        });

        //make it automatic, but this doesn't work properly, I'm stuck...
        setInterval(function() {
            var current = parseInt($('li.selected a').data('links-to').split('_')[1],10);
            var idx=current-1;
            var max = $('.carouselLinks li a').length;
            idx = (current<max) ? (idx+1):0;
            $('.object-new a:eq('+idx+')').trigger('click');
        }, 3000);

        /**
         * This is where the animation, i.e. fade, is performing.
         * I find it quite convenient to use bind/trigger principle as it's easier to maintain
         */
        tabs.find('a').bind('slides.swap', function() {
            var self = $(this),
                selfIndex = self.parent().index(),
                targetSlide = slides.eq(selfIndex);

            //fade in/out slides
            slides.filter('.active').stop(true, false).fadeOut(speed, function() {
                $(this).removeClass('active');
            });
            targetSlide.stop(true, false).fadeIn(speed).addClass('active');

            tabs.removeClass('selected');
            self.parent().addClass('selected');
        });
    }
};

HM.init();



		/*------------------------
		9 Magnific Popup
		--------------------------*/
		$('.popup-gallery').magnificPopup({
			delegate: 'a.popup-img',
			tLoading: 'Loading image #%curr%...',
			type: 'image',
			mainClass: 'mfp-img-mobile',
			gallery: {
				navigateByImgClick: true,
				enabled: true,
				preload: [0, 1]
			},
			image: {
				tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
			}
		});
		$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
			type: 'iframe',
			disableOn: 700,
			mainClass: 'mfp-fade',
			preloader: false,
			removalDelay: 160,
			fixedContentPos: false
		});




		/*------------------------
		counter
		--------------------------*/
		// $('.timer').countTo();



		/*------------------------
		10 Wow Animation
		--------------------------*/
		var wow = new WOW({
			boxClass: 'wow',
			animateClass: 'animated',
			offset: 0,
			mobile: false,
			live: true
		});
		wow.init();





		/*------------------------
		11 Contact From
		--------------------------*/
		$('#contact').submit(function(e) {
			var form_data = $(this).serialize();
			var flag = 0;
			e.preventDefault(); // Prevent Default Submission
			$('.require').each(function() {
				if ($.trim($(this).val()) == '') {
					$(this).css("border", "1px solid red");
					e.preventDefault(); // Prevent Default Submission
					flag = 1;
				} else {
					$(this).css("border", "1px solid grey");
					flag = 0;
				}
			});
			if (grecaptcha.getResponse() == "") {
				flag = 1;
				alert('Please verify Recaptch');

			} else {
				flag = 0;
			}
			if (flag == 0) {
				console.log(form_data);
				$.ajax({
						url: 'php/contact-form.php',
						type: 'POST',
						data: form_data, // it will serialize the form data
					})
					.done(function(data) {
						console.log("successfully");
						$("#result").html('Form was successfully submitted.');
						$('#contact')[0].reset();
					})
					.fail(function() {
						alert('Ajax Submit Failed ...');
						console.log("fail");

					});
			}
		});
	});

})(jQuery);