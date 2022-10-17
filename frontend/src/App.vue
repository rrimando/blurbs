<template>
  <div id="app">
    <BlurbsComponent />
  </div>
</template>

<script>
import BlurbsComponent from "./components/Blurbs.vue";
export default {
  name: "App",
  components: {
    BlurbsComponent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>