
jQuery(document).ready(function ($) {
	$('input').on('keypress', function () {
		$('.has-error').hide();	
	});
});

//------------------------------------>>>>>>>>
/*
$(document).ready(function () {
    // body...
var loginLink = document.getElementById('login');
if (loginLink) {
	loginLink.onclick = function() { navigator.id.request(); };
};

var logoutLink = document.getElementById('logout');
if (logoutLink) {
	logoutLink.onclick = function() { navigator.id.logout(); };
};

var currentUser = '{{ user.email }}' || null;
var csrf_token = ' {{ csrf_token }} ';
console.log(currentUser);

navigator.id.watch({
	loggedInUser: currentUser,
	onlogin: function(assertion) {
		$.post('/accounts/login', {assertion: assertion, csrfmiddlewaretoken: csrf_token})
		.done(function() { window.location.reload(); })
		.fail(function() { navigator.id.logout(); });
	},
	onlogout: function() {
		$.post('/accounts/logout')
		.always(function() { window.location.reload(); });
	}
});   


});
*/




