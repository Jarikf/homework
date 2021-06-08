<template>
  <div class="hello">
    <h1 v-if="eventsCount !== null">
      {{ eventsCount }} events occurred in last {{ maxAge }} seconds.
    </h1>
    <h1 v-else>Could not load events count, refresh page to try again.</h1>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { statisticsModule } from "@/store/statistics";

@Options({
  props: {
    maxAge: Number,
    updatePeriod: Number,
  },
})
export default class ServerEventsInfo extends Vue {
  maxAge!: number;
  updatePeriod!: number;

  get eventsCount(): number | null {
    return statisticsModule.eventsCount;
  }

  created(): void {
    statisticsModule.loadEventsCount(this.maxAge);
    setInterval(
      () => statisticsModule.loadEventsCount(this.maxAge),
      this.updatePeriod * 1000
    );
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
