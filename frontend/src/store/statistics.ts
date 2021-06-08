import { VuexModule, Module, Mutation, Action } from "vuex-class-modules";
import statisticsApi from "@/api";

@Module
class StatisticsModule extends VuexModule {
  // state
  eventsCount: number | null = null;

  // mutations
  @Mutation
  setEventsCount(events: number | null) {
    this.eventsCount = events;
  }

  // actions
  @Action
  async loadEventsCount(maxAge: number) {
    const count = await statisticsApi.getEventsCount(maxAge);
    this.setEventsCount(count);
  }
}

// register module (could be in any file)
import store from "./index";
export const statisticsModule = new StatisticsModule({
  store,
  name: "statistics",
});
