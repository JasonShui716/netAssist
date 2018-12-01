window.onload = function(){
	var dirList = document.querySelectorAll('a.dir');
	console.log(dirList);
	alert('aaa');
	dirList.forEach(function(dirItem){
		dirItem.setAttribute("href",document.URL+dirItem.text);		
		console.log(dirItem.getAttribute("href"));
	});
}
