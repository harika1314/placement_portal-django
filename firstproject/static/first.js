AOS.init({
	duration:1200,
});
/*$(document).on('click','.navbar-right li a',function(){
		$(this).addClass('active').siblings().removeClass('active');
		});
		
		let mybutton = document.getElementById("btn-back-to-top");

		// When the user scrolls down 20px from the top of the document, show the button
		window.onscroll = function () {
		scrollFunction();
		};
		
		function scrollFunction() {
		if (
		document.body.scrollTop > 20 ||
		document.documentElement.scrollTop > 20
		) {
		mybutton.style.display = "block";
		} else {
		mybutton.style.display = "none";
		}
		}
		// When the user clicks on the button, scroll to the top of the document
		mybutton.addEventListener("click", backToTop);
		
		function backToTop() {
		document.body.scrollTop = 0;
		document.documentElement.scrollTop = 0;
		}*/
		/*new Swiper('.clients-slider', {
			speed: 400,
			loop: true,
			autoplay: {
			  delay: 5000,
			  disableOnInteraction: false
			},
			slidesPerView: 'auto',
			pagination: {
			  el: '.swiper-pagination',
			  type: 'bullets',
			  clickable: true
			},
			breakpoints: {
			  320: {
				slidesPerView: 2,
				spaceBetween: 40
			  },
			  480: {
				slidesPerView: 3,
				spaceBetween: 60
			  },
			  640: {
				slidesPerView: 4,
				spaceBetween: 80
			  },
			  992: {
				slidesPerView: 6,
				spaceBetween: 120
			  }
			}
		  });*/

//Menu icon
function myMenu(){
	if(document.getElementById("mini_navbar").style.display == "block"){
		document.getElementById("mini_navbar").style.display = "none";
	}
	else{
		document.getElementById("mini_navbar").style.display = "block";
	}
	
}
function toggle_menu(){
	document.getElementById("mini_navbar").style.display = "none";
}

//sticky nav bar
window.addEventListener("scroll",function(){
	var header = document.querySelector("header");
	header.classList.toggle("sticky",window.scrollY>0);
})		