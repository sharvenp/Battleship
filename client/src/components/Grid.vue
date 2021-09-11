<template>
  <div class="grid">
    <div v-for="i in 9" :key="i" class="container d-block noselect">
      <div v-if="i == 1">
        <div class="header m-2 d-table-cell">
          <p class="header-text">&nbsp;</p>
        </div>
        <div v-for="j in 8" :key="j" class="header d-table-cell">
          <p class="mt-4">{{ j }}</p>
        </div>
      </div>
      <div v-else>
        <div class="header m-2 d-table-cell">
          <p class="mt-4">{{ String.fromCharCode(i + 63) }}</p>
        </div>
        <div
          v-for="j in 8"
          :key="j"
          :class="
            `cell ${isOpponent && 'hover'} d-table-cell ${!isOpponent &&
              isSquareOcupied(i - 2, j - 1) &&
              'ocupied'}`
          "
          @click="isOpponent ? sendHit(i - 2, j - 1) : () => {}"
        >
          {{
            grid[i - 2][j - 1] === 2
              ? "❌"
              : grid[i - 2][j - 1] === 1
              ? "💥"
              : ""
          }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Grid",
  props: ["ships", "isOpponent"],
  data() {
    return {
      grid: [],
    };
  },
  beforeMount() {
    this.grid = Array(8)
      .fill(0)
      .map(() => Array(8).fill(0));
  },
  methods: {
    isSquareOcupied(i, j) {
      return this.ships.some((ship) => ship.ocupiesSquare(i, j));
    },
    sendHit(i, j) {
      if (this.isOpponent && this.$parent.currTurn !== 0) {
        return;
      }

      if (this.grid[i][j] !== 0) {
        return;
      }

      this.grid[i][j] = this.isSquareOcupied(i, j) ? 1 : 2;
      this.ships.forEach((ship) => ship.processHit(i, j));
      this.$emit("updateTurn");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cell {
  width: 4rem;
  height: 4rem;
  border: solid 1px rgba(0, 0, 0, 0.5);
  background-color: rgba(80, 80, 80, 0.2);
  font-size: 2rem;
}

.hover:hover {
  background-color: rgba(255, 0, 0, 0.5);
}

.header {
  width: 4rem;
  height: 4rem;
  border: none;
  font-weight: bold;
}

.ocupied {
  background-color: rgba(20, 20, 20, 0.4);
}
</style>
