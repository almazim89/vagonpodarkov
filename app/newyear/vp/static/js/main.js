$(document).ready(function(){
	$("#send_message").on("click", function(){
	    $('#feedback').fadeIn();
	    $(this).hide();
	});
	$("#close_form").on("click", function(){
		$('#feedback').fadeOut();
		$("#send_message").show();
	});
});