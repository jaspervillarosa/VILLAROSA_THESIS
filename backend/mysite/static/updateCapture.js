const supportsFileSystemAccessAPI = 
'getAsFileSystemHandle' in DataTransferItem.prototype;

const elem = document.querySelector(".container-Capture")
const fileCapture = document.querySelector(".fileCapture")
const headerCapture = elem.querySelector(".headerCapture")
const reset = elem.querySelector(".resetCapture")
const predict = elem.querySelector(".predictCapture")

// prevent navigation 
// elem.addEventListener('dragover', (e) => {
//     e.preventDefault();
// })

// // Visually highlight the dropzone 
// elem.addEventListener('dragenter', (e) => {
//     e.preventDefault();
//     elem.classList.add("active")
//     dragText.textContent = "Release to Upload"

// })

// elem.addEventListener('dragleave', (e) => {
//     elem.classList.remove("active")
//     dragText.textContent = "Drag & Drop to Upload File"
// })

// elem.addEventListener('drop', (e) => {
//     e.preventDefault()
//     elem.classList.add("active")
//     dragText.textContent = "File Uploaded"
//     fileInput.files = e.dataTransfer.files
//     console.log(fileInput.files)
    
// })

// reset.addEventListener('click', (e) => {
//     e.preventDefault()
//     elem.classList.remove("active");
//     fileInput.value="";
//     dragText.textContent="Drag and Drop to Upload File";

// })

fileCapture.addEventListener('click', (e) => {
    if(fileCapture.value!=null){
        headerCapture.textContent = "Image Captured"
        elem.classList.add("active")
    }
    else{
        dragText.textContent="Capture Media";
    }
})


