window.onload= setheaders;


function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
            	cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            	break;
            }
        }
    }
    return cookieValue;
}

function setheaders(){
	$.ajaxSetup({
		headers: { 'X-CSRFToken': getCookie('csrftoken') }
	});

}

function edituser(id){ 

	$.ajax({
		method: 'POST',
		url: '../edituser/',
		data: {'iduser': id,
	},
	success: function (data) {
		$("#containerform").html(data);
	},
	error: function (data) {
		alert('Error de conexión');
	}
});

}
