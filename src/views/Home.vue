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
    
      
        <div ref="chart" class="chart" id="theChart"></div>
      
    
    <!-- <div class="row">
      <ol v-if="linksArray.length > 0">
        <li v-for="link in linksArray">
          {{ link.name }}
        </li>
      </ol>  
    </div> -->
  </div>
</template>
<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
import echarts from 'echarts'
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
      // myChart: echarts.init(document.getElementById('main')),
      // chart: {},
      
    }
  },
  components: {
    HelloWorld
  },
  methods: {
    justChecking(url) {
      console.log('hi',url)
    },

    getJSONFromScrape (url) {
      this.linksArray = []
      let path = 'http://localhost:5000/links'
      // let path = 'http://ubuntu@52.27.159.135:5000/' + url
      console.log('url',url)
      axios.get(path, {
        params: {
          destination: url 
        }
      })
      .then(response => {
        this.linksArray = response.data.Links
        console.log(response.data.Links)
        this.updateChart(response.data.Links, url)
      })
      .catch(error => {
        console.log(error)
      })      
  },
  
  updateChart(urls, url) {
    var myChart = echarts.init(this.$refs['chart']);
    console.log('urls',urls)
    // let links = []
    // urls.forEach(function(link) {
    //   links.push(link)
    // })
    // console.log('links in array',links)

    urls.forEach(function(node) {
      node.itemStyle = null;
      node.symbolSize = 20;
      // Use random x, y
      node.x = node.y = null;
      node.draggable = true;
    })
    
    var option = {        
      title : {
          text: 'hi',
          subtext: 'subtext',
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
      },
      series : [
          {
              type:'graph',
              layout: 'force',
              name : "experiment graph",
              categories : [
                  {
                      name: url
                  },                  
              ],
              itemStyle: {
                  normal: {
                      label: {
                          show: true,
                          textStyle: {
                              color: 'rgba(0,0,0,1)'
                          }
                      },
                      linkStyle: {
                          type: 'curve'
                      }
                  },
                  emphasis: {
                      label: {
                          show: false
                          // textStyle: null      // 默认使用全局文本样式，详见TEXTSTYLE
                      },
                      nodeStyle : {
                          // r: 30
                      },
                      linkStyle : {}
                  }
              },
              // useWorker: false,
              // minRadius : 35,
              // maxRadius : 45,
              // gravity: 1.1,
              // scaling: 3.1,
              // roam: 'move',
              data: urls,
              links: [
                // {source : '丽萨-乔布斯', target : '乔布斯', weight : 1, name: '女儿'},

              ]
          }
      ]
    };
    
    var myChart = echarts.init(this.$refs['chart']);
    myChart.setOption(option)
    console.log('option in thing',option.series[0].nodes)
    }
  },

  mounted: function () {  
    // init echarts
    
  }
}
</script>

<style scoped>
#chartDiv {
  align-content: center;
 
}

#theChart {
  height:700px;
  position: relative;
  border: solid;
}

canvas{
  margin: 0 auto;
}

</style>
