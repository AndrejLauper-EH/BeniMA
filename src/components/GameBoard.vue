<script setup>
import { ref } from 'vue'

const board = ref(Array(24).fill(0))
const player = ref(1) // human = 1, ai = 2
const message = ref('Dein Zug')

function indexToStyle(i) {
  const coords = [
    [0,0],[50,0],[100,0],
    [0,50],[50,50],[100,50],
    [0,100],[50,100],[100,100],
    [12.5,12.5],[50,12.5],[87.5,12.5],
    [12.5,50],[87.5,50],
    [12.5,87.5],[50,87.5],[87.5,87.5],
    [25,25],[50,25],[75,25],
    [25,50],[75,50],
    [25,75],[50,75],[75,75],
  ]
  const [x,y] = coords[i]
  return {
    left: `${x}%`,
    top: `${y}%`
  }
}

async function play(i) {
  if (board.value[i] !== 0 || player.value !== 1) return
  board.value[i] = 1
  message.value = 'KI denkt...'
  const res = await fetch('http://localhost:5000/ai/move', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ board: board.value })
  })
  const data = await res.json()
  if (data.position !== null) {
    board.value[data.position] = 2
  }
  message.value = 'Dein Zug'
}
</script>

<template>
  <div class="board">
    <div v-for="(field, index) in board" :key="index" class="field" :style="indexToStyle(index)" @click="play(index)">
      <span v-if="field === 1" class="stone player"></span>
      <span v-else-if="field === 2" class="stone ai"></span>
    </div>
  </div>
  <p>{{ message }}</p>
</template>

<style scoped>
.board {
  position: relative;
  width: 400px;
  height: 400px;
  background: #fafafa;
  border: 2px solid #333;
  margin: 0 auto;
}
.field {
  position: absolute;
  width: 20px;
  height: 20px;
  transform: translate(-50%, -50%);
  cursor: pointer;
}
.stone {
  display: block;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}
.stone.player {
  background: #007bff;
}
.stone.ai {
  background: #dc3545;
}
</style>
