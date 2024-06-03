import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import dataV from '@jiaminghi/data-view'
import VueParticles from 'vue-particles'
import './plugins/axios.js'
import './plugins/element.js'

import "swiper/swiper.min.css"
import * as echarts from 'echarts';
import "@/utils/echarts-wordcloud.min.js"

Vue.use(VueParticles)
Vue.use(dataV)
Vue.config.productionTip = false

Vue.prototype.$echarts = echarts

//axios发送http请求的目标地址的基础路径
Vue.prototype.$axios.defaults.baseURL = 'http://localhost:8000'

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')