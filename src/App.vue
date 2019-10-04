<template>
  <div id="app">
    <img style="{height: auto; max-width: 30%}" alt="Vue logo" src="./assets/logo.png">
    <p class="title is-3 is-size-4-mobile is-spaced has-text-info has-text-centered">Nearby Places</p>
    <Search msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import Search from './components/Search.vue'

export default {
  name: 'app',
  components: {
    Search
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

#app > img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  height:auto;
  max-width:30%;
}
</style>
