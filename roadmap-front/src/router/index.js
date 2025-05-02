import { createRouter, createWebHistory } from 'vue-router'
import RoadmapView from '../views/RoadmapView.vue'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
        path: '/roadmap',
        name: 'roadmap',
        component: RoadmapView
    },
    {
        path: '/',
        name: 'home',
        component: HomeView
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router