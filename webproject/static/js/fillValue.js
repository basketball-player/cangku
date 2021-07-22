// fillValue.js
// 向表格中填入数值
var i = 1;
{% for row in data %}
  var j = 1;
  {% for item in row %}
    //alert(i.toSting()+" " + j.toString());
    var id = "cell_" + i.toString() + j.toString();
    var cell = document.getElementById(id);
    cell.innerText = "{{item}}";
    j++;
  {% endfor %}
  i++;
{% endfor %}

//for(var i=1; i<=n_jobs; i++) {
//  for(var j=1; j<7; j++) {
////    var id = "cell_" + i.toString() + j.toString();
////    var cell = document.getElementById(id);
////    cell.innerText = data.i.j;
//  }
//}