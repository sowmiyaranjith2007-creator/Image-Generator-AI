# 🎨 AI Image Generator

An AI-powered text-to-image generation application developed by **Sowmiya** using Python, Streamlit, Hugging Face Diffusers, PyTorch, and Stable Diffusion.

---

## 👩‍💻 Developed By

**Sowmiya**

Undergraduate student interested in:

- Data Science
- Artificial Intelligence
- Generative AI
- Large Language Models
- Python
- Web Development

---

## 📌 About The Project

AI Image Generator is an interactive web application that generates images from text prompts.

Users can enter a description such as:

```text
A cute cat sitting in a flower garden, digital art
```

The application sends the prompt to a Stable Diffusion model and displays the generated image in the Streamlit interface.

The project uses Hugging Face Diffusers for the text-to-image pipeline. [web:31]

---

## ✨ Features

- Generate images from text prompts.
- Uses a Stable Diffusion model.
- Simple and interactive Streamlit interface.
- Supports positive prompts.
- Supports negative prompts.
- Adjustable inference steps.
- Adjustable guidance scale.
- Seed control for reproducible images.
- Supports CPU and GPU execution.
- Download generated images as PNG files.
- Displays the generated image inside the application.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- PyTorch
- Hugging Face Diffusers
- Transformers
- Accelerate
- Safetensors
- Pillow
- Stable Diffusion

---

## 🤖 Model Used

```text
LanguageMachines/stable-diffusion-2-1-base
```

The Stable Diffusion pipeline generates images based on text input. Hugging Face Diffusers provides the pipeline used for loading the model and generating the image. [web:1][web:6]

---

## 📂 Project Structure

```text
AI-Image-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/AI-Image-Generator.git](https://github.com/your-username/AI-Image-Generator.git)
```

Replace `your-username` with your GitHub username.

### 2. Open the project folder

```bash
cd AI-Image-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ How To Run

Run the Streamlit application using:

```bash
streamlit run app.py
```

If the above command does not work, use:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

Streamlit applications can be started from the terminal using the `streamlit run` command. [web:64][web:66]

---

## 🖼️ How To Use

1. Open the application.
2. Enter a text prompt.
3. Enter a negative prompt if required.
4. Select inference steps from the sidebar.
5. Select guidance scale.
6. Select a seed value.
7. Click the **Generate Image** button.
8. Wait for the image to be generated.
9. Click **Download Image** to save the generated image.

---

## 📝 Example Prompts

### Cute Cat

```text
A cute cat sitting in a flower garden, digital art
```

### Futuristic City

```text
A futuristic city at night, neon lights, cinematic digital art
```

### Fantasy Castle

```text
A magical castle floating in the clouds, fantasy art
```

### Nature Landscape

```text
A beautiful green valley surrounded by mountains, realistic landscape
```

### Cartoon Character

```text
A cute cartoon girl reading a book under a tree, colorful digital art
```

---

## 🚫 Example Negative Prompt

```text
blurry, low quality, distorted, bad anatomy, extra fingers, watermark
```

---

## 🔄 How It Works

1. The user enters a text prompt.
2. The application loads the Stable Diffusion model.
3. The prompt is passed to the Diffusers pipeline.
4. The model processes the text prompt.
5. An image is generated.
6. The generated image is displayed in Streamlit.
7. The user can download the generated image.

The Diffusers text-to-image workflow loads a pretrained pipeline and passes a prompt to generate an image. [web:34][web:95]

---

## 🧠 Important Notes

- The first run may take longer because the model needs to be downloaded.
- An internet connection is required during the first model download.
- GPU execution is faster than CPU execution.
- CPU image generation may take several minutes.
- Generated images are created for educational and creative purposes.
- Do not upload large model files to GitHub.

---

## 🚀 Future Improvements

- Add image history.
- Add multiple model choices.
- Add image-to-image generation.
- Add custom image width and height.
- Add more art styles.
- Add image gallery.
- Add dark mode.
- Add user authentication.
- Deploy the application online.
- Add Streamlit Cloud deployment.
- Add prompt suggestions.
- Add image metadata.

---

## 📄 License

This project is created for educational and learning purposes.

---

## 🙏 Acknowledgements

- Hugging Face Diffusers
- Streamlit
- PyTorch
- Stable Diffusion
- Python Community

---

## 📬 Contact

Created by **Sowmiya**

GitHub: `https://github.com/your-username`

---

## ⭐ Support

If you like this project, please give the repository a star on GitHub.

---

### Made with Python and Generative AI by Sowmiya 💜
