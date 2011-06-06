function addRow(form){
	key = form.key.value;
	value = form.value.value;
	input = $("<input/>").attr("name", key)
			.attr("value", value).attr("type", "text");
	row = $("<tr></tr>").append("<td>"+key+": </td>")
			.append($("<td></td>").append(input));
	$("#submitrow").before(row);
	$("#addrow").hide("fast");
	return false;
}

function showAddRow(){
	$("#addrow").show("fast");
	return false;
}

function hideAddRow(){
	$("#addrow").hide("fast");
	return false;
}

function deleteRow(input){
	$("#tr_"+input.name).remove();
	return false;
}


