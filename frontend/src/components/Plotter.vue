<template>
    <div>
      <div>
        <label>Train Folder:</label>
        <input v-model="trainFolder" placeholder="Enter train folder path" />
        <button @click="plotTrain">Plot Train</button>
      </div>
      <div>
        <label>Test Folder:</label>
        <input v-model="testFolder" placeholder="Enter test folder path" />
        <button @click="plotTest">Plot Test</button>
      </div>
      <div>
        <h2>Train Results:</h2>
        <img v-if="trainImage" :src="trainImage" alt="Train Results" />
      </div>
      <div>
        <h2>Test Results:</h2>
        <img v-if="testImage" :src="testImage" alt="Test Results" />
      </div>
    </div>
  </template>
  
  <script>
  import { plotTrain, plotTest } from '../api/plot.js';
  
  export default {
    data() {
      return {
        trainFolder: '',
        testFolder: '',
        trainImage: null,
        testImage: null,
      };
    },
    methods: {
      async plotTrain() {
        this.trainImage = await plotTrain(this.trainFolder);
      },
      async plotTest() {
        this.testImage = await plotTest(this.testFolder);
      },
    },
  };
  </script>
  