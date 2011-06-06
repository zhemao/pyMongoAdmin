function newDocument(form){
	db = form.db.value;
	coll = form.coll.value;
	window.location = "/db/"+db+"/coll/"+coll+"/doc/new";
	return false;
}

function makeSure(){
	return confirm("Are you sure you want to do this? This action cannot be undone.");
}
