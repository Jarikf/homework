<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <h1>This is a home webpage</h1>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({
  components: {},
})
export default class Home extends Vue {}
</script>
