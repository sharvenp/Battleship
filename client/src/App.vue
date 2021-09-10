<template>
  <h1 class="mt-5 font-weight-bold big noselect">BATTLESHIP!</h1>
  <Game />
</template>

<script>
import Game from "./views/Game.vue";

export default {
  name: "App",
  components: {
    Game,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Rubik&display=swap");

#app {
  font-family: "Rubik", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome and Opera */
}

.big {
  font-size: 4rem;
  font-weight: bold;
}
</style>
