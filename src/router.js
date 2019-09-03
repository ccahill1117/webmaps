import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Experiment from './views/Experiment.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/experiment',
      name: 'experiment',
      component: Experiment
    }    
  ]
})
