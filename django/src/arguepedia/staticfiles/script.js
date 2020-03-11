function revealMessage(){
	document.getElementById("hiddenMessage").style.display= 'block';
}

function revealTuple(){
	document.getElementById("id_title").style.display="none";
}

$('#id_argument_type').on('change', function(){
  var mainselection = this.value; // get the selection value
  if (mainselection == "expert"){


  document.getElementById("id_title").style.display="none";
	}
    });