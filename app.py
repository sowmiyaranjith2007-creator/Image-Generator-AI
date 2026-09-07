import asyncio
import sys

# Windows connection warning fix
if sys.platform == "win32":
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )

import streamlit as st
import torch
from diffusers import StableDiffusionPipeline


# Page settings
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="centered"
)


# Application title
st.title("🎨 AI Image Generator")
st.write("Enter a text prompt and generate an AI image.")


# Hugging Face model
MODEL_ID = "LanguageMachines/stable-diffusion-2-1-base"


# Load model only once
@st.cache_resource(show_spinner="Loading Stable Diffusion model...")
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    if device == "cuda":
        dtype = torch.float16
    else:
        dtype = torch.float32

    pipeline = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=dtype
    )

    pipeline = pipeline.to(device)

    return pipeline, device


# Prompt input
prompt = st.text_area(
    "Enter your prompt",
    value="A cute cat sitting in a flower garden, digital art",
    height=100
)


# Negative prompt
negative_prompt = st.text_input(
    "Negative prompt (optional)",
    placeholder="blurry, low quality, distorted, extra fingers"
)


# Settings
st.sidebar.header("Image Settings")

steps = st.sidebar.slider(
    "Inference steps",
    min_value=10,
    max_value=50,
    value=20
)

guidance = st.sidebar.slider(
    "Guidance scale",
    min_value=1.0,
    max_value=15.0,
    value=7.5,
    step=0.5
)

seed = st.sidebar.number_input(
    "Seed",
    min_value=0,
    max_value=999999,
    value=42,
    step=1
)


# Generate button
if st.button("✨ Generate Image", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        try:
            with st.spinner("Generating image... Please wait."):

                pipeline, device = load_model()

                generator = torch.Generator(device=device).manual_seed(
                    int(seed)
                )

                result = pipeline(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    num_inference_steps=steps,
                    guidance_scale=guidance,
                    height=512,
                    width=512,
                    generator=generator
                )

                image = result.images[0]

            st.image(
                image,
                caption=prompt,
                use_container_width=True
            )

            image_bytes = bytearray()
            from io import BytesIO

            image_buffer = BytesIO()
            image.save(image_buffer, format="PNG")
            image_bytes = image_buffer.getvalue()

            st.download_button(
                label="⬇️ Download Image",
                data=image_bytes,
                file_name="ai_generated_image.png",
                mime="image/png",
                use_container_width=True
            )

            st.success(f"Image generated successfully using {device.upper()}.")

        except Exception as error:
            st.error("Image generation failed.")
            st.exception(error)


# Information section
st.markdown("---")
st.subheader("Example Prompts")

st.write("🐱 A cute cat sitting in a flower garden, digital art")
st.write("🏰 A magical castle in the clouds, fantasy art")
st.write("🌌 A futuristic city under a galaxy sky, cinematic")
