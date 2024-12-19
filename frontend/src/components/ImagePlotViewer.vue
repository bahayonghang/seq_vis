<template>
  <div id="app">
    <h1>Image Plot Viewer</h1>
    <div>
      <label for="folderPath">Select Folder:</label>
      <input type="file" webkitdirectory @change="onFolderSelect" />
    </div>
    <div>
      <button :disabled="!folderPath" @click="fetchTrainImage">View Train Results</button>
      <button :disabled="!folderPath" @click="fetchTestImage">View Test Results</button>
    </div>
    <div v-if="trainImage">
      <h2>Train Results:</h2>
      <img :src="trainImage" alt="Train Results" />
    </div>
    <div v-if="testImage">
      <h2>Test Results:</h2>
      <img :src="testImage" alt="Test Results" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      folderPath: "", // 保存用户选择的文件夹路径
      trainImage: null,
      testImage: null,
    };
  },
  methods: {
    onFolderSelect(event) {
      const files = event.target.files;
      if (files.length > 0) {
        this.folderPath = files[0].webkitRelativePath.split("/")[0];
        alert(`Selected folder: ${this.folderPath}`);
      }
    },
    async fetchTrainImage() {
      try {
        const formData = new FormData();
        formData.append("folder_path", this.folderPath);

        const response = await fetch("/plot_test_train", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          this.trainImage = URL.createObjectURL(await response.blob());
        } else {
          const error = await response.json();
          alert(error.error);
        }
      } catch (error) {
        alert("An error occurred: " + error.message);
      }
    },
    async fetchTestImage() {
      try {
        const formData = new FormData();
        formData.append("folder_path", this.folderPath);

        const response = await fetch("/plot_test", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          this.testImage = URL.createObjectURL(await response.blob());
        } else {
          const error = await response.json();
          alert(error.error);
        }
      } catch (error) {
        alert("An error occurred: " + error.message);
      }
    },
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 20px;
  color: #f0f0f0;
  background-color: #2c3e50;
  padding: 20px;
}
input {
  margin: 10px;
}
button {
  margin: 10px;
}
img {
  max-width: 100%;
  height: auto;
  margin-top: 20px;
}
</style>
