function editPart(  partID ){
	alert( partID );
	$.get({
		url : '/edit/' + partID 
	});
}
