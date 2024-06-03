import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: sessionStorage.getItem('user') ? JSON.parse(sessionStorage.getItem('user')) : {},
    fisherman: sessionStorage.getItem('fisherman') ? JSON.parse(sessionStorage.getItem('fisherman')) : {},
    Authorization: sessionStorage.getItem('Authorization') ? sessionStorage.getItem('Authorization') : '',
    isLogin: false
  },
  mutations: {
    setUser(state, value) {
      state.user = value;
      sessionStorage.setItem("user", JSON.stringify(value));
    },
    setFisherman(state, value) {
      state.fisherman = value;
      sessionStorage.setItem("fisherman", JSON.stringify(value));
    },
    setAuthorization(state, value) {
      state.Authorization = value;
      sessionStorage.setItem("Authorization", value);
    },
    setLogin(state, value) {
      state.isLogin = value;
    }
  },
  actions: {
  },
  modules: {
  }
})
