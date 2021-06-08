import axios from "axios";

const statisticsAxios = axios.create({
  baseURL: `${process.env.VUE_APP_BACKEND_ADDRESS}/api/v1/`,
  timeout: 1000,
});

export default {
  async getEventsCount(maxAge: number): Promise<number | null> {
    try {
      const result = await statisticsAxios.get("mediaserver-events/count/", {
        params: { max_age: maxAge },
      });
      return result.data.count;
    } catch (error) {
      return null;
    }
  },
};
