<template>
  <div>
    <h3 v-if="!isAllShipsPlaced()" class="mt-3">Place your ships...</h3>
    <div class="btn-group d-block mt-3" role="group">
      <button
        v-for="(ship, idx) in ships"
        :key="idx"
        type="button"
        :class="
          `m-1 btn btn-${
            selectedShip && selectedShip.name === ship.name
              ? 'warning'
              : 'primary'
          }`
        "
        @click="selectShip(idx)"
      >
        {{ ship.name }} ({{ ship.size }})
      </button>
    </div>
    <button type="button" class="mt-2 btn btn-secondary" @click="rotateShip">
      Rotate
    </button>
    <div class="align-items-center grid noselect">
      <div v-for="i in 9" :key="i" class="container d-block">
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
              `cell d-table-cell ${isSquareOcupied(i - 2, j - 1) && 'ocupied'}`
            "
            @click="placeShip()"
            @mouseenter="hoverCell(i - 2, j - 1)"
            @mouseleave="resetSquares"
          ></div>
        </div>
      </div>
    </div>
    <button
      v-if="isAllShipsPlaced()"
      type="button"
      class="mt-4 btn btn-danger"
      @click="start"
    >
      Ready!
    </button>
  </div>
</template>

<script>
import { Ship } from "../classes";

export default {
  name: "Placement",
  data() {
    return {
      direction: { dr: 1, dc: 0 },
      selectedShip: null,
      valid: false,
      ships: [
        new Ship("Carrier", 5),
        new Ship("Battleship", 4),
        new Ship("Cruiser", 3),
        new Ship("Submarine", 3),
        new Ship("Destroyer", 2),
      ],
    };
  },
  beforeMount() {
    this.selectedShip = this.ships[0];
  },
  methods: {
    isAllShipsPlaced() {
      return this.ships.every((ship) => ship.placed);
    },
    isSquareOcupied(i, j) {
      return this.ships.some((ship) => ship.ocupiesSquare(i, j));
    },
    resetSquares() {
      if (this.selectedShip === undefined) {
        return;
      }

      this.selectedShip.squares = [];
    },
    hoverCell(i, j) {
      if (this.selectedShip === undefined) {
        return;
      }

      this.valid = true;
      let count = 0;
      let currRow = i;
      let currCol = j;
      let placementSquares = [];
      while (count < this.selectedShip.size) {
        if (currRow > 7 || currRow < 0 || currCol > 7 || currCol < 0) {
          this.valid = false;
          break;
        }

        if (
          this.ships.filter((ship) => ship.ocupiesSquare(currRow, currCol))
            .length > 0
        ) {
          this.valid = false;
          break;
        }

        count++;
        placementSquares.push([currRow, currCol]);
        currRow += this.direction.dr;
        currCol += this.direction.dc;
      }

      if (this.valid) {
        this.selectedShip.squares = placementSquares;
      } else {
        this.resetSquares();
      }
    },
    placeShip() {
      if (!this.valid || this.selectedShip === undefined) {
        return;
      }

      this.selectedShip.placed = true;
      this.valid = false;

      if (!this.isAllShipsPlaced()) {
        let idx = 0;
        while (idx < this.ships.length) {
          if (!this.ships[idx].placed) {
            break;
          }
          idx++;
        }
        this.selectedShip = this.ships[idx];
      } else {
        this.selectedShip = undefined;
      }
    },
    selectShip(idx) {
      this.selectedShip = this.ships[idx];
      this.selectedShip.placed = false;
    },
    rotateShip() {
      this.direction.dr = (this.direction.dr + 1) % 2;
      this.direction.dc = (this.direction.dc + 1) % 2;
    },
    start() {
      this.$emit("ready", this.ships);
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
}

.header {
  width: 4rem;
  height: 4rem;
  border: none;
  font-weight: bold;
}

.grid {
  margin-right: 4rem;
}

.ocupied {
  background-color: rgba(20, 20, 20, 0.4);
}
</style>
