fetch('http://127.0.0.1:8000/getdata').then(function(response){
  return response.json();
 }).then(function(jsondata){
  console.log(jsondata);
 });