<template>

  <div class="table-container">
    <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Rating</th>
            <th>Address</th>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
            <tr v-for="(result,number) in results">
              <td>{{number}}</td>
              <td>{{result.name}}</td>
              <td>{{result.rating}}</td>
              <td>{{result.vicinity}}</td>
              <td>{{result.geometry.location.lat}}</td>
              <td>{{result.geometry.location.lng}}</td>
              <td>{{result.types[0]}}</td>
            </tr>  
        </tbody>
    </table>
  </div>

</template>

<script>
export default {
  name: 'ResultTable',
  props: ['results'],
  data () {
    return {
      
    }
  },

  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
