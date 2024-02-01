import { createWebHistory, createRouter } from 'vue-router'
import UserPage from '../components/UserPage.vue'
import AdminPage from '../components/AdminPage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: UserPage,
    },
    {
      path: '/admin',
      component: AdminPage,
    }
  ]
})

export default router