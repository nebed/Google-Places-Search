import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import './../node_modules/bulma/css/bulma.css';
import router from './router';

Vue.config.productionTip = false
window.axios = axios;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
