// createTable.js
var str = "";
for (var i = 1; i <= n_jobs;i++) {
  str += "<tr class=\"text-center\">";
  for(var j = 1; j < 7;j++) {
      id = "cell_" + i.toString() + j.toString();
      str += "<td id=\"" + id + "\"></td>";
  }
  str += "<td id=\"" +"cell_" + i.toString() + "8\">" +
  "<input class=\"btn btn-default\"  value=查看 id=\"button_" + i.toString()+"\">"+ "</td>";
  str += "</tr>";
}
document.write(str);