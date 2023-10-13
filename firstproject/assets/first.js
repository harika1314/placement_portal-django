AOS.init({
	duration:1200,
});
$(document).on('click','.navbar-right li a',function(){
		$(this).addClass('active').siblings().removeClass('active');
		});