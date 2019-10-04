<template>
  <div class="container is-fluid">

    <div class="columns is-mobile is-centered">
      <div class="column is-half">
            
             <div class="field">
                <label class="label">Location</label>
                <div class="control">
                  <input class="input" type="text" v-model="location" placeholder="Latitude,Longitude (ex: 6.4280552,3.4044348)">
                </div>
              </div>
              <div class="field">
                <label class="label">Radius (metres)</label>
                <div class="control">
                  <input class="input" type="number" v-model="radius" placeholder="Radius in metres">
                </div>
              </div>

              <div class="field">
                <label class="label">Keyword</label>
                <div class="control">
                  <input class="input" type="text" v-model="keyword" placeholder="Keyword (name or address - optional)">
                </div>
              </div>

              <div class="field">
              <label class="label">Place Type</label>
                <div class="control is-expanded">
                  <div class="select is-fullwidth">
                    <select v-model="type">
                      <option value="">Choose Place Type</option>
                      <option value="accounting">accounting</option>
                      <option value="airport">airport</option>
                      <option value="amusement_park">amusement_park</option>
                      <option value="aquarium">aquarium</option>
                      <option value="art_gallery">art_gallery</option>
                      <option value="atm">atm</option>
                      <option value="bakery">bakery</option>
                      <option value="bank">bank</option>
                      <option value="bar">bar</option>
                      <option value="beauty_salon">beauty_salon</option>
                      <option value="bicycle_store">bicycle_store</option>
                      <option value="book_store">book_store</option>
                      <option value="bowling_alley">bowling_alley</option>
                      <option value="bus_station">bus_station</option>
                      <option value="cafe">cafe</option>
                      <option value="campground">campground</option>
                      <option value="car_dealer">car_dealer</option>
                      <option value="car_rental">car_rental</option>
                      <option value="car_repair">car_repair</option>
                      <option value="car_wash">car_wash</option>
                      <option value="casino">casino</option>
                      <option value="cemetery">cemetery</option>
                      <option value="church">church</option>
                      <option value="city_hall">city_hall</option>
                      <option value="clothing_store">clothing_store</option>
                      <option value="convenience_store">convenience_store</option>
                      <option value="courthouse">courthouse</option>
                      <option value="dentist">dentist</option>
                      <option value="department_store">department_store</option>
                      <option value="doctor">doctor</option>
                      <option value="drugstore">drugstore</option>
                      <option value="electrician">electrician</option>
                      <option value="electronics_store">electronics_store</option>
                      <option value="embassy">embassy</option>
                      <option value="fire_station">fire_station</option>
                      <option value="florist">florist</option>
                      <option value="funeral_home">funeral_home</option>
                      <option value="furniture_store">furniture_store</option>
                      <option value="gas_station">gas_station</option>
                      <option value="grocery_or_supermarket">grocery_or_supermarket</option>
                      <option value="gym">gym</option>
                      <option value="hair_care">hair_care</option>
                      <option value="hardware_store">hardware_store</option>
                      <option value="hindu_temple">hindu_temple</option>
                      <option value="home_goods_store">home_goods_store</option>
                      <option value="hospital">hospital</option>
                      <option value="insurance_agency">insurance_agency</option>
                      <option value="jewelry_store">jewelry_store</option>
                      <option value="laundry">laundry</option>
                      <option value="lawyer">lawyer</option>
                      <option value="library">library</option>
                      <option value="light_rail_station">light_rail_station</option>
                      <option value="liquor_store">liquor_store</option>
                      <option value="local_government_office">local_government_office</option>
                      <option value="locksmith">locksmith</option>
                      <option value="lodging">lodging</option>
                      <option value="meal_delivery">meal_delivery</option>
                      <option value="meal_takeaway">meal_takeaway</option>
                      <option value="mosque">mosque</option>
                      <option value="movie_rental">movie_rental</option>
                      <option value="movie_theater">movie_theater</option>
                      <option value="moving_company">moving_company</option>
                      <option value="museum">museum</option>
                      <option value="night_club">night_club</option>
                      <option value="painter">painter</option>
                      <option value="park">park</option>
                      <option value="parking">parking</option>
                      <option value="pet_store">pet_store</option>
                      <option value="pharmacy">pharmacy</option>
                      <option value="physiotherapist">physiotherapist</option>
                      <option value="plumber">plumber</option>
                      <option value="police">police</option>
                      <option value="post_office">post_office</option>
                      <option value="primary_school">primary_school</option>
                      <option value="real_estate_agency">real_estate_agency</option>
                      <option value="restaurant">restaurant</option>
                      <option value="roofing_contractor">roofing_contractor</option>
                      <option value="rv_park">rv_park</option>
                      <option value="school">school</option>
                      <option value="secondary_school">secondary_school</option>
                      <option value="shoe_store">shoe_store</option>
                      <option value="shopping_mall">shopping_mall</option>
                      <option value="spa">spa</option>
                      <option value="stadium">stadium</option>
                      <option value="storage">storage</option>
                      <option value="store">store</option>
                      <option value="subway_station">subway_station</option>
                      <option value="supermarket">supermarket</option>
                      <option value="synagogue">synagogue</option>
                      <option value="taxi_stand">taxi_stand</option>
                      <option value="tourist_attraction">tourist_attraction</option>
                      <option value="train_station">train_station</option>
                      <option value="transit_station">transit_station</option>
                      <option value="travel_agency">travel_agency</option>
                      <option value="university">university</option>
                      <option value="veterinary_care">veterinary_care</option>
                      <option value="zoo">zoo</option>
                    </select>
                  </div>
                </div>
              </div>

              <div class="field">
                <div class="control is-centered">
                  <button @click="getPlaces()" :class="{'is-loading' : isLoading}" class="button is-outlined is-link is-fullwidth has-margin-top-3">Find</button>
                </div>
              </div>

      </div>
    </div>
 
        <div class="columns is-mobile is-centered">
          <div class="column is-four-fifths">
              <ResultTable :results="results"/>
              <a class="button is-primary is-fullwidth" :disabled="disabled" :href="csv" download="places.csv">Download CSV</a>
          </div>
        </div>


    </div>
</template>

<script>
import ResultTable from '../components/ResultTable.vue';
export default {
  components : { ResultTable },
  name: 'Search',
  props: {
    msg: String
  },
  data () {
    return {
      location:"",
      radius: "500",
      keyword:"",
      type:"",
      isLoading:false,
      results: [],
      csv: "",
      disabled: true,
    }
  },

  methods: {

    getPlaces() {
      this.isLoading = true;
          axios.get(window.location.href + 'find?location=' + this.location + '&radius=' + this.radius + '&keyword=' + this.keyword + '&type=' + this.type).then(response => {this.isLoading=false; this.results = response.data.results; this.downloadCSV(this.results); return this.results;}).catch(error => { this.isLoading=false; return console.log(error);});
    },

    convertArrayOfObjectsToCSV(args) {  
        var result, ctr, keys, columnDelimiter, lineDelimiter, data;

        data = args.data || null;
        if (data == null || !data.length) {
            return null;
        }

        columnDelimiter = args.columnDelimiter || ',';
        lineDelimiter = args.lineDelimiter || '\n';

        keys = Object.keys(data[0]);

        result = '';
        result += keys.join(columnDelimiter);
        result += lineDelimiter;

        data.forEach(function(item) {
            ctr = 0;
            keys.forEach(function(key) {
                if (ctr > 0) result += columnDelimiter;

                result += item[key];
                ctr++;
            });
            result += lineDelimiter;
        });

        return result;
    },

     downloadCSV(results) {
      var csvarray = [];
      console.log(results);
      results.forEach(function( ob ) {
        csvarray.push({'Name':ob.name.replace(/,/g, ""), 'Rating':ob.rating, 'Address':ob.vicinity.replace(/,/g, ""), 'Latitude':ob.geometry.location.lat, 'Longitude':ob.geometry.location.lng, 'Place Type':ob.types[0]});
      });
      var csv = this.convertArrayOfObjectsToCSV({
            data: csvarray
        });

      if (csv == null) return;

        if (!csv.match(/^data:text\/csv/i)) {
            csv = 'data:text/csv;charset=utf-8,' + csv;
        }
        this.csv = encodeURI(csv);
        this.disabled = false;

    }
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
