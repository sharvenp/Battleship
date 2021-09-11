import { createWebHistory, createRouter } from "vue-router";
import Home from "./views/Home.vue";
import Game from "./views/Game.vue";

let routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/play",
    name: "game",
    component: Game,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
