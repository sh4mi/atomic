(function ($) {
"use strict";


$('.menu-open').on('click',function(){
	$('.off-canvas-menu').addClass('active');
})

$('.close-icon').on('click',function(){
	$('.off-canvas-menu ,.off-canvas-overlay').removeClass('active');
})
$('.menu-open').on('click',function(){
	$('.off-canvas-overlay').addClass('active');
})

$('.off-canvas-overlay').on('click',function(){
	$('.off-canvas-overlay ,.off-canvas-menu').removeClass('active');
})


// counterup
$('.counter').counterUp({
	delay: 10,
	time: 1000
});
// counterup-end


// sticky
$(window).on('scroll', function () {
	var scroll = $(window).scrollTop();
	if (scroll < 200) {
		$("#header-sticky").removeClass("sticky-bar");
	} else {
		$("#header-sticky").addClass("sticky-bar");
	}
});
// sticky-end

// scrollToTop
$.scrollUp({
	scrollName: 'scrollUp', // Element ID
	topDistance: '300', // Distance from top before showing element (px)
	topSpeed: 300, // Speed back to top (ms)
	animation: 'fade', // Fade, slide, none
	animationInSpeed: 200, // Animation in speed (ms)
	animationOutSpeed: 200, // Animation out speed (ms)
	scrollText: '<i class="fas fa-long-arrow-alt-up"></i>', // Text for element
	activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
});

// WOW active
if ($(".wow").length) {
	var wow = new WOW({
		boxClass: 'wow',      // animated element css class (default is wow)
		animateClass: 'animated', // animation css class (default is animated)
		offset: 20,          // distance to the element when triggering the animation (default is 0)
		mobile: true,       // trigger animations on mobile devices (default is true)
		live: true,       // act on asynchronously loaded content (default is true)
	});
	wow.init();
}


//  AOS Animation
if ($("[data-aos]").length) {
	AOS.init({
		duration: 1000,
		mirror: true
	});
}

$('#mobile-menu').meanmenu({
    meanMenuContainer:".mobile-menu",
    meanScreenWidth:"991",
});

$('.slider-c-active').owlCarousel({
    loop:true,
    margin:30,
	items:1,
	dots:true,
    responsive:{
        0:{
            items:1
        },
        767:{
            items:1
        },
        992:{
            items:1
        }
    }
})


$('.brand-active').owlCarousel({
    loop:true,
    margin:0,
	items:5,
	dots:false,
    responsive:{
        0:{
            items:1
        },
        767:{
            items:3
        },
        992:{
            items:5
        }
    }
})


/* magnificPopup img view */
$('.popup-image').magnificPopup({
	type: 'image',
	gallery: {
	  enabled: true
	}
});

/* magnificPopup video view */
$('.popup-video').magnificPopup({
	type: 'iframe'
});



$('.grid').imagesLoaded( function() {
	// init Isotope
	var $grid = $('.grid').isotope({
	  itemSelector: '.grid-item',
	  percentPosition: true,
	  masonry: {
		// use outer width of grid-sizer for columnWidth
		columnWidth: 1,
	  }
	});
});

// filter items on button click
$('.portfolio-menu').on( 'click', 'button', function() {
  var filterValue = $(this).attr('data-filter');
  $grid.isotope({ filter: filterValue });
});	



//for menu active class
$('.portfolio-menu button').on('click', function(event) {
	$(this).siblings('.active').removeClass('active');
	$(this).addClass('active');
	event.preventDefault();
});

// google map

function basicmap() {
	// Basic options for a simple Google Map
	// For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
	var mapOptions = {
		// How zoomed in you want the map to start at (always required)
		zoom: 11,
		scrollwheel: false,
		// The latitude and longitude to center the map (always required)
		center: new google.maps.LatLng(23.810331, 90.412521), // New York
		// This is where you would paste any style found on Snazzy Maps.
		styles:[
			{
				"featureType": "administrative.country",
				"elementType": "geometry",
				"stylers": [
					{
						"visibility": "simplified"
					},
					{
						"hue": "#ff0000"
					}
				]
			}
		]
	};
	// Get the HTML DOM element that will contain your map 
	// We are using a div with id="map" seen below in the <body>
	var mapElement = document.getElementById('contact-map');

	// Create the Google Map using our element and options defined above
	var map = new google.maps.Map(mapElement, mapOptions);

	// Let's also add a marker while we're at it
	var marker = new google.maps.Marker({
		position: new google.maps.LatLng(23.810331, 90.412521),
		map: map,
		title: 'Cryptox'
	});
}
if ($('#contact-map').length != 0) {
	google.maps.event.addDomListener(window, 'load', basicmap);
}
// google-map-end

})(jQuery);	