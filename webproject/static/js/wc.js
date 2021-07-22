// 为查看词云的按钮绑定事件
for (var i=1; i<=n_jobs; i++) {
  document.getElementById("button_"+i.toString()).addEventListener(
    'click',
    function(){
      var cellId = "cell_" + this.id.slice(7) + "1";             // 这按钮对应岗位名称所在单元格的Id
      var jobName = document.getElementById(cellId).innerText;   // 这按钮对应的岗位名称
      var wcName = cityName + "_" + jobName;                     // 词云文件名
      var wcPath = "/static/wc/" + wcName + ".png";              // 词云路径
      //alert(wcName);
      // 打开一个新窗口
      OpenWindow=window.open("", "newwin", "height=750, width=950, top=100, left=250, toolbar=no, scrollbars="
        + scroll + ",menubar=no");
      OpenWindow.document.write("<html>");
      OpenWindow.document.write("<title>"+jobName+"的岗位描述词云图</title>");
      OpenWindow.document.write("<bod y>");
      OpenWindow.document.write("<img alt=\"\" src=" + wcPath + ">");
      OpenWindow.document.write("</body>");
      OpenWindow.document.write("</html>");
      OpenWindow.document.close()
    },
    false
  );
}