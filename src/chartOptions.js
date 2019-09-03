var options = {        
  title : {
      text: 'hi',
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
          data: '',
          
          links: '',
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

export default options