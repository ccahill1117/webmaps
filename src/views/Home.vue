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
      <!-- <button @click=justChecking(url)>Scrape site</button> -->
    </div>
    <div class="row">
      <ol v-if="linksArray.length > 0">
        <li v-for="link in linksArray">
          {{ link.url }}
        </li>
      </ol>  
    </div>
    <div ref="chart" class="chart" style="width: 600px;height:400px;"></div>
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
      url: '',
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
      let path = 'http://ubuntu@52.27.159.135:5000/' + url
      console.log('url',url)
      axios.get(path)
      .then(response => {
        this.linksArray = response.data.Links
        console.log(this.linksArray)
      })
      .catch(error => {
        console.log(error)
      })
    }
  }, 
  mounted: function () {  
    // init echarts
    var myChart = echarts.init(this.$refs['chart']);
    console.log('mychart',myChart)
    
        // based on prepared DOM, initialize echarts instance
        // var myChart = echarts.init(document.getElementById('chart'));

        // specify chart configuration item and data
        var option = {
            title: {
                text: 'ECharts entry example'
            },
            tooltip: {},
            legend: {
                data:['Sales']
            },
            xAxis: {
                data: ["shirt","cardign","chiffon shirt","pants","heels","socks"]
            },
            yAxis: {},
            series: [{
                name: 'Sales',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        };

        // use configuration item and data specified to show chart
        myChart.setOption(option)

  }
}
</script>
