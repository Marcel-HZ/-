import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import UnderWaterSystem from '../views/UnderWaterSystem.vue'
import DataCenter from '../views/DataCenter.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import AI from '../views/AI.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Index',
    component: Index,
    meta: { 
        name: '主要信息',
        showHeader: true,
        showBackground: true,
    }
}, 
{
    path: '/underWaterSystem',
    name: 'UnderWaterSystem',
    component: UnderWaterSystem,
    meta: { 
        name: "水下系统" ,
        showHeader: true,
        showBackground: true,
    }
}, 
{
    path: '/dataCenter',
    name: 'DataCenter',
    component: DataCenter,
    meta: { 
        name: "数据中心" , 
        showHeader: true,
        showBackground: true,
    }
},
{
    path: '/ai',
    name: 'AI',
    component: AI,
    meta: { 
        name: "智能中心" , 
        showHeader: true,
        showBackground: true,
    }
},
{
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { 
        name: "退出登录" , 
        showHeader: false,
        showBackground: false,
    }
},
{
    path: '/admin',
    name: 'Admin',
    meta: { 
        name: "管理员登录" , 
        showHeader: false,
        showBackground: false,
    }
},
{
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { 
        name: "登录" , 
        showHeader: false,
        showBackground: false,
    }
},
{
    path: '/register',
    name: 'Register',
    component: Register,
    meta: { 
        name: "注册" , 
        showHeader: false,
        showBackground: false,
    }
},
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})


// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {
    if (to.path === '/admin') {
        window.location.href = 'http://127.0.0.1:8000/xadmin';
      } else {
        	// 设置标题
            if (to.meta.title) {
                document.title = to.meta.title
            }

            if (to.path === '/login' || to.path === '/register' || to.path === '/') {
                if(to.path === '/login' || to.path === '/register') {
                    sessionStorage.removeItem('Authorization');
                }
                next();
            } else {
                let token = sessionStorage.getItem('Authorization');
                if (token === null || token === '') {
                    next('/login');
                } else {
                    next();
                }
            }
      }
});



export default router 