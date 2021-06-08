<template>
  <div class="statistics">
    <server-events-info :max-age="60" :update-period="60" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import ServerEventsInfo from "@/components/statistics/ServerEventsInfo.vue";

@Options({
  components: {
    ServerEventsInfo,
  },
})
export default class Statistics extends Vue {}
</script>
