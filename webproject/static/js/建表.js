var str = "";
for (var i = 1; i <= 10;i++)
{
    str += "<tr>";
    for(var j = 1; j < 8;j++){
        id = "cell_" + i.toString() + j.toString();
        str += "<td id=\"" + id + "\"></td>";
    }
    str += "<td id=\"" +"cell_" + i.toString() + "8\">" +
    "<input class=\"btn btn-default\"  value=查看 id=\"button_" + i.toString()+"\">"+ "</td>";
    str += "</tr>";
}
document.write(str);