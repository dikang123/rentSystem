<template>
  <div id="app">
    <v-hello></v-hello>
    <v-choose></v-choose>
  </div>
</template>

<script>
  import HelloWorld from './components/HelloWorld';
  import Choose from './components/choose';

  export default{
    name: 'app',
    components: {
      'v-hello': HelloWorld,
      'v-choose': Choose
    }
  };
</script>

<style lang="stylus" rel="stylesheet/stylus">
  body
    padding: 0
    margin: 0

</style>
