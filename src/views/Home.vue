<template>
  <div class="home">
    <div class="row">
      <h2>This web application will return a list of anchor tags based on the URL entered, in the visualization below!</h2>
    </div>
    <div class="row">
      <label for="input">if you want to scrape https://www.nytimes.com, type 'nytimes.com'</label>
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
import { options } from '@/chartOptions'

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
      // chartOptions: options
    }
  },
 
  methods: {
    justChecking(url) {
      console.log('hi',url)
    },

    getJSONFromScrape (url) {
      this.linksArray = []
      // let path = 'http://ubuntu@52.27.159.135:5000/links'
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
        this.updateChart(response.data.Links.links, response.data.Links.connects, url)
      })
      .catch(error => {
        console.log(error)
      })  
    },
  
  updateChart(urls, links, url) {
    var myChart = echarts.init(this.$refs['chart'])    
    var option = {        
      title : {
          text: 'Webpage Maps',
          subtext: 'subtext',
          x:'right',
          y:'bottom'
      },
      tooltip : {
          // trigger: 'item',
          // formatter: '{a} : {b}'
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
                      // name: url
                      name: 'a'
                  },                  
              ],
              itemStyle: {
                  normal: {
                      label: {
                          show: true,
                          textStyle: {
                              color: '#333'
                          }
                      },
                      linkStyle: {
                          type: 'curve'
                      }
                  },
                  emphasis: {
                      label: {
                          show: false
                      },
                      nodeStyle : {
                          r: 30
                      },
                      lineStyle: {
                        normal: {
                            color: 'source',
                            curveness: 0.3
                        }
                    }
                  }
              },
              force: {
                    repulsion: 300
              },
              // useWorker: false,
              minRadius : 55,
              maxRadius : 45,
              gravity: 1.1,
              scaling: 3.1,
              roam: 'move',
              data: urls,
              
              links: links,
              lineStyle: {
                normal: {
                    opacity: 0.9,
                    width: 2,
                    curveness: 0,
                }
              },
              symbolSize : 5,
              edgeSymbol: ['circle', 'arrow'],
              
          }
      ]
    }
    
    var myChart = echarts.init(this.$refs['chart']);
    myChart.setOption(option)
    myChart.on('click', function() {
      console.log('hi')
    })


    console.log('data',option.series[0].nodes)
    console.log('links',option.series[0].links)

    }
  },

  mounted: function () {  
    // init echarts
    // this.getJSONFromScrape('hello.com')
    
  }
}
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
