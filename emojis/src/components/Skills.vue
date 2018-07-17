<template>
  <div class="hello">
    <div class="holder">
      <ul>
        <li v-for="(data,index) in skills" :key='index'>
          {{data.skill}}
        </li>
      </ul>
<<<<<<< HEAD
      <div v-bind:class="alertObject">  
=======
      <div v-bind:class="{alert: showAlert}">
        
>>>>>>> 6c5ccc0daf47a8622b83fb981f8cb6436404adb8
      </div>      
      
    </div>   
  </div>
</template>

<script>
export default {
  name: 'Skills',
  data(){
    return {
      skills: [
        {"skill" : "Vue.js"},
        {"skill" : "Frontend Developer"}
      ],
<<<<<<< HEAD
      alertObject : {
        alert : true
      }
=======
      showAlert : true
>>>>>>> 6c5ccc0daf47a8622b83fb981f8cb6436404adb8
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style  scoped>
<<<<<<< HEAD
.holder {
  background: #fff;
}

ul{
  margin: 0;
  padding: 0;
  list-style-type: none;
}

ul li {
  padding: 20px;
  font-size: 1.3em;
  background-color: #E0EDF4;
  border-left: 5px solid #3EB3F6;
  margin-bottom: 2px;
  color: #3E5252; 
}

p{
  text-align: center;
  padding: 30px 0;
  color: gray;
}
.container{
  box-shadow: 0px 0px 40px lightgray;
=======
ul{
  list-style-type: none;
}

.alert{
  background-color: "yellow";
  width: 100%;
  height: 30px;
>>>>>>> 6c5ccc0daf47a8622b83fb981f8cb6436404adb8
}

</style>
