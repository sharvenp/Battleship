<template>
  <div class="container">
    <h1 v-if="winner" class="mt-3 text-danger">{{ winner }} WINS!</h1>
    <h3 v-if="!winner && !isPlacing" class="mt-5 text-danger">
      <div v-if="currTurn !== 0">
        AI IS THINKING
        <div class="spinner-border text-danger">
          <span class="visually-hidden"></span>
        </div>
      </div>
      <div v-else>
        YOUR TURN
      </div>
    </h3>
    <Placement v-if="isPlacing" @ready="OnReady" />
    <div class="grid-div d-flex mt-5" v-else>
      <Grid
        class="mr-5"
        :ships="this.ships"
        :isOpponent="false"
        ref="playerGrid"
      />
      <Grid
        class="ml-5"
        :ships="this.opponentShips"
        :isOpponent="true"
        @updateTurn="onUpdate"
        ref="opponentGrid"
      />
    </div>
  </div>
</template>

<script>
import { parseConfiguration } from "../classes";
import Placement from "./Placement.vue";
import Grid from "../components/Grid.vue";
import axios from "axios";

export default {
  name: "Game",
  data() {
    return {
      isPlacing: true,
      ships: [],
      opponentShips: [],
      currTurn: 0,
      winner: undefined,
    };
  },
  components: {
    Placement,
    Grid,
  },
  methods: {
    async OnReady(ships) {
      this.isPlacing = false;
      this.ships = ships;

      // get opponent ships configuration
      const response = await axios.get(
        `${process.env.VUE_APP_BOT_SERVER_URL}/vector-api/get-configuration`
      );
      this.opponentShips = parseConfiguration(response.data);
    },
    async onUpdate() {
      if (this.currTurn !== 0 || this.winner) {
        return;
      }

      if (this.opponentShips.every((ship) => ship.destroyed)) {
        this.winner = "PLAYER";
        return;
      }

      // get opponent move
      this.currTurn = 1;

      await new Promise((resolve) => setTimeout(resolve, 1000)); // add a little delay

      const requestData = JSON.stringify({
        grid: this.$refs.playerGrid.grid,
      });

      const response = await axios.post(
        `${process.env.VUE_APP_BOT_SERVER_URL}/vector-api/get-move`,
        requestData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      this.$refs.playerGrid.sendHit(response.data.i, response.data.j);

      if (this.ships.every((ship) => ship.destroyed)) {
        this.winner = "AI";
        return;
      }

      this.currTurn = 0;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  display: grid;
  justify-content: center;
  align-items: center;
}

.grid-div {
  justify-content: center;
  align-items: center;
  width: 90vw;
}
</style>
