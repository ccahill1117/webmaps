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
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

import axios from 'axios'

export default {
  name: 'home',
  data() {
    return {
      url: '',
      linksArray: []
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
      let path = 'http://localhost:5000/' + url
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
  } 
}
</script>
