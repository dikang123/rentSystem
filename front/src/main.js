// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import Vuex from 'vuex';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(Vuex); // 通过 Vue.use() 注册使用插件
Vue.use(ElementUI);
Vue.config.productionTip = false;
Vue.use(VueRouter); // 安装这个插件
Vue.use(VueResource); // 全局注册
Vue.prototype.axios = axios;

const routes = [
  {
    path: '/',
    name: 'app',
    component: App
  }
];
const router = new VueRouter({
  linkActiveClass: 'acvite',
  routes
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
});
