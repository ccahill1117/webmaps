<template>
  <div class="home">
    <div class="row">
      <label for="input">if you want to scrape https://www.nytimes.com, just type 'nytimes.com'</label>
    </div>
    <div class="row">
      <input type="text" v-model='url'>
    </div>
    <div class="row">
      <button @click=getJSONFromScrape(url)>Scrape site</button>
    </div>
      <div ref="chart" class="chart" id="theChart">
      </div>
  </div>
</template>
<script>

import axios from 'axios'
import echarts from 'echarts'
import { Script } from 'vm';
require('echarts/lib/chart/bar')
// include tooltip and title component
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')


export default {
  name: 'home',
  data() {
    return {
      url: 'hello.com',
      linksArray: [],
    }
  },
  components: {
   
  },
  methods: {
    justChecking(url) {
      console.log('hi',url)
    },

    getJSONFromScrape (url) {
      this.linksArray = []
      let path = 'http://localhost:5000/links'
      axios.post(path, {
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': "*",
        },
        params: {
          links: url
        }
      })
      .then(response => {
        this.linksArray = response.data.Links
        // this.linksArray.push(originPoint)
        // console.log('dataBack',response.data)
        this.updateChart(response.data.Links.links, response.data.Links.connects, url)
      })
      .catch(error => {
        console.log(error)
      })  
    },
  
  updateChart() {
    var myChart = echarts.init(this.$refs['chart']);

  var option = {
    title : {
        text: '人物关系：乔布斯',
        subtext: '数据来自人立方',
        x:'right',
        y:'bottom'
    },
    tooltip : {
        trigger: 'item',
        formatter: '{a} : {b}'
    },
    toolbox: {
        show : true,
        feature : {
            restore : {show: true},
            magicType: {show: true, type: ['force', 'chord']},
            saveAsImage : {show: true}
        }
    },
    legend: {
        x: 'left',
        data:['家人','朋友']
    },
    series : [
        {
            type:'force',
            name : "人物关系",
            ribbonType: false,
            categories : [
                {
                    name: '人物'
                },
                {
                    name: '家人',
                    symbol: 'diamond'
                },
                {
                    name:'朋友'
                }
            ],
            itemStyle: {
                normal: {
                    label: {
                        show: true,
                        textStyle: {
                            color: '#333'
                        }
                    },
                    nodeStyle : {
                        brushType : 'both',
                        borderColor : 'rgba(255,215,0,0.4)',
                        borderWidth : 1
                    }
                },
                emphasis: {
                    label: {
                        show: false
                        // textStyle: null      // 默认使用全局文本样式，详见TEXTSTYLE
                    },
                    nodeStyle : {
                        //r: 30
                    },
                    linkStyle : {}
                }
            },
            minRadius : 15,
            maxRadius : 25,
            gravity: 1.1,
            scaling: 1.2,
            draggable: false,
            linkSymbol: 'arrow',
            steps: 10,
            coolDown: 0.9,
            //preventOverlap: true,
            nodes:[
                {
                    category:0, name: '乔布斯', value : 10,
                    symbol: 'image://http://www.damndigital.com/wp-content/uploads/2010/12/steve-jobs.jpg',
                    symbolSize: [60, 35],
                    draggable: true,
                    itemStyle: {
                        normal: {
                            label: {
                                position: 'right',
                                textStyle: {
                                    color: 'black'
                                }
                            }
                        }
                    }
                },
                {category:1, name: '丽萨-乔布斯',value : 2},
                {category:1, name: '保罗-乔布斯',value : 3},
                {category:1, name: '克拉拉-乔布斯',value : 3},
                {category:1, name: '劳伦-鲍威尔',value : 7},
                {category:2, name: '史蒂夫-沃兹尼艾克',value : 5},
                {category:2, name: '奥巴马',value : 8},
                {category:2, name: '比尔-盖茨',value : 9},
                {category:2, name: '乔纳森-艾夫',value : 4},
                {category:2, name: '蒂姆-库克',value : 4},
                {category:2, name: '龙-韦恩',value : 1},
            ],
            links : [
                {source : '丽萨-乔布斯', target : '乔布斯', weight : 1, name: '女儿', itemStyle: {
                    normal: {
                        width: 1.5,
                        color: 'red'
                    }
                }},
                {source : '乔布斯', target : '丽萨-乔布斯', weight : 1, name: '父亲', itemStyle: {
                    normal: { color: 'red' }
                }},
                {source : '保罗-乔布斯', target : '乔布斯', weight : 2, name: '父亲'},
                {source : '克拉拉-乔布斯', target : '乔布斯', weight : 1, name: '母亲'},
                {source : '劳伦-鲍威尔', target : '乔布斯', weight : 2},
                {source : '史蒂夫-沃兹尼艾克', target : '乔布斯', weight : 3, name: '合伙人'},
                {source : '奥巴马', target : '乔布斯', weight : 1},
                {source : '比尔-盖茨', target : '乔布斯', weight : 6, name: '竞争对手'},
                {source : '乔纳森-艾夫', target : '乔布斯', weight : 1, name: '爱将'},
                {source : '蒂姆-库克', target : '乔布斯', weight : 1},
                {source : '龙-韦恩', target : '乔布斯', weight : 1},
                {source : '克拉拉-乔布斯', target : '保罗-乔布斯', weight : 1},
                {source : '奥巴马', target : '保罗-乔布斯', weight : 1},
                {source : '奥巴马', target : '克拉拉-乔布斯', weight : 1},
                {source : '奥巴马', target : '劳伦-鲍威尔', weight : 1},
                {source : '奥巴马', target : '史蒂夫-沃兹尼艾克', weight : 1},
                {source : '比尔-盖茨', target : '奥巴马', weight : 6},
                {source : '比尔-盖茨', target : '克拉拉-乔布斯', weight : 1},
                {source : '蒂姆-库克', target : '奥巴马', weight : 1}
            ]
        }
    ]
  };    

    
    myChart.setOption(option)

    },

    focus(param) {
    var data = param.data;
    var links = option.series[0].links;
    var nodes = option.series[0].nodes;
    if (
        data.source != null
        && data.target != null
    ) { //点击的是边
        var sourceNode = nodes.filter(function (n) {return n.name == data.source})[0];
        var targetNode = nodes.filter(function (n) {return n.name == data.target})[0];
        console.log("选中了边 " + sourceNode.name + ' -> ' + targetNode.name + ' (' + data.weight + ')');
    } else { // 点击的是点
        console.log("选中了" + data.name + '(' + data.value + ')');
    }
}
// myChart.on(ecConfig.EVENT.CLICK, focus)

// myChart.on(ecConfig.EVENT.FORCE_LAYOUT_END, function () {
//     console.log(myChart.chart.force.getPosition());
// });
  },

  mounted: function () {  
    // init echarts
    
  }
}


// var ecConfig = require('echarts/config');




</script>
<style scoped>
#chartDiv {
  align-content: center;
 
}

#theChart {
  height:800px;
  position: relative;
  border: solid;
}

canvas{
  margin: 0 auto;
}

</style>
