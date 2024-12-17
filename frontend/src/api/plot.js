export async function plotTrain(folderPath) {
    const formData = new FormData();
    formData.append('folder_path', folderPath);
  
    const response = await fetch('/plot/train', {
      method: 'POST',
      body: formData,
    });
  
    if (response.ok) {
      return URL.createObjectURL(await response.blob());
    } else {
      console.error('Error plotting train results');
      return null;
    }
  }
  
  export async function plotTest(folderPath) {
    const formData = new FormData();
    formData.append('folder_path', folderPath);
  
    const response = await fetch('/plot/test', {
      method: 'POST',
      body: formData,
    });
  
    if (response.ok) {
      return URL.createObjectURL(await response.blob());
    } else {
      console.error('Error plotting test results');
      return null;
    }
  }
  