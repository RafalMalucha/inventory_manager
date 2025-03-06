  <script lang="js">
    import TestComponent from './components/TestComponent.vue';

    export default {
      name: "App",
      components: {
        TestComponent,
      },
    };
  </script>

  <template>
    <div id="app">
      <h1>skibidiii</h1>
      <TestComponent />
    </div>
  </template>
  
  <style>
  body {
    font-family: Arial, sans-serif;
    text-align: center;
  }
  </style>
  