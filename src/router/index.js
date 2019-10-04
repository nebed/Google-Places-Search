import Vue from 'vue'
import Router from 'vue-router'

let routes = [

{
	path: '/',
	component: require('../components/Search.vue').default
},

];
Vue.use(Router);
export default new Router({
  routes,
  mode: 'history'
})