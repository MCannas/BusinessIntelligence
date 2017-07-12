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
	$("#sentences").hide();
	$("#query").hide();
	$("#tables").hide();
	
	$.ajaxSetup({
		headers: { 'X-CSRFToken': getCookie('csrftoken') }
	});

}

function startconnection(id){ 

	$.ajax({
		method: 'POST',
		url: '../getsentences/',
		data: {'idconnection': id,
	},
	success: function (data) {
		$("#panellist").hide();
		$("#query").show();
		var sentences = JSON.parse(data.sentences);
		var tds = "";
		for(var i = 0; i< sentences.length; i++){
			tds += "<p draggable='true' ondragstart='drag(event)'>" + sentences[i].fields.name + " " + "</p>";
		}
		$("#sentences").html(tds);
		$("#sentences").show();

	},
	error: function (data) {
		alert('Error de conexión');
	}
});


	$.ajax({
		method: 'POST',
		url: '../gettables/',
		data: {'idconnection': id,
	},
	success: function (data) {
		var tables = JSON.parse(data)
		var tds = "";
		for(var i = 0; i<tables.length;i++){
			tds += "<p draggable='true' ondragstart='drag(event)'>" + tables[i].name + " " + "</p>";
		}
		$("#tables").html(tds);
		$("#tables").show();
	},
	error: function (data) {
		alert('Error de conexión');
	}
});

}


function allowDrop(ev) {
	ev.preventDefault();
}

function drag(ev) {
	ev.dataTransfer.setData("text", ev.target.innerHTML);
}

function drop(ev) {
	ev.preventDefault();
	var data = ev.dataTransfer.getData("text");
	$("#query").append(data);
}





