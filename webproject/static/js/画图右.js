// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main2'));
// 指定图表的配置项和数据
var option = {
title: {
text: '第一个 ECharts 实例',
subtext:"数据来自前程无忧网站",
left:'center',
},
tooltip: {},
legend: {
data:['岗位1','岗位2','岗位3','岗位4'],
bottom:0
},
xAxis:[{
type:"category",
data: ["工作年限1","工作年限1","工作年限1","工作年限1","工作年限1","工作年限1"]
}],
splitArea:{
show:false
},
yAxis: {
name:"薪资",
min:0,
max:40,
interval:8,
show:true,
grid:false
},
series: [{
name: '岗位1',
type: 'bar',
data: [5, 20, 36, 10, 10, 20]
},
{
name: '岗位2',
type: 'bar',
data: [5, 20, 36, 10, 10, 20]
},
{
name: '岗位3',
type: 'bar',
data: [5, 20, 36, 10, 10, 20]
},
{
name: '岗位4',
type: 'bar',
data: [5, 20, 36, 10, 10, 20]
}
]
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);