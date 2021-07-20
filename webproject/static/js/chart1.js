// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('chart1'));
// 指定图表的配置项和数据
var option = {
    title: {
        text: '月薪-学历关系图',
        left:'center'
    },
    grid:{
        show:false
    },
    toolbox: {
        show:true,
        feature:{
            saveAsImage:{
                title:'保存为图片',
                type:'png'
            },
            dataZoom:{
                show:true
            },
            dataView:{
                show: true,

                type:['bar','line']
            },
            magicType:{
                show:true,
                type:['line','bar']
            }
        }
    },
    legend: {
        data: ['0','1','2','3','4'],
        bottom:0
    },
    xAxis:[{
        type:"category",
        data: ["初中", "高中", "中专", "大专", "本科", "硕士", "博士"]
    }],
//    splitArea:{
//        show:false
//    },
    yAxis: {
        name:"薪资",
        //min:0,
        //max:40,
        //interval:8

    },
    series: [{
        name: '岗位1',
        type: 'bar',
        data: {{MSM1}}
    },
    {
        name: '岗位2',
        type: 'bar',
        data: {{MSM2}}
    },
    {
        name: '岗位3',
        type: 'bar',
        data: {{MSM3}}
    },
    {
        name: '岗位4',
        type: 'bar',
        data: {{MSM4}}
    },
    {
        name: '岗位5',
        type: 'bar',
        data: {{MSM5}}
    }


    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);