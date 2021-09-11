<template>
  <div class="firstDivision">
    <div class="verticalCenter">
      <h1 class="mt-5 font-weight-bold extra-big noselect">BATTLESHIP!</h1>
      <button type="button" class="mt-5 btn btn-danger big round" @click="play">
        PLAY
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  methods: {
    play() {
      this.$router.push({
        name: "game",
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.round {
  border-radius: 1.3rem;
}

.firstDivision {
  display: table;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}

.firstDivision .verticalCenter {
  text-align: center;
  display: table-cell;
  vertical-align: middle;
}
</style>
