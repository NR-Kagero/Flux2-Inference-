FLUX.2 Text-to-Image Generation with stable-diffusion-cpp
======================================================

This README documents the Diffusion.py script, which implements an image generation pipeline using the Python bindings for the high-performance, C/C++ based stable-diffusion-cpp library.

This setup is notable for its use of the FLUX.2 diffusion model and a Mistral LLM for prompt processing, both loaded in the highly optimized GGUF format, enabling efficient generation on consumer-grade hardware.

KEY FEATURES
------------

- High-Performance Backend: Utilizes the stable-diffusion-cpp library for fast, low-memory inference, leveraging the highly optimized GGUF (GGML Universal Format) file structure.
- Model Components: The pipeline loads three critical components:
    1. Diffusion Model (FLUX.2): The core text-to-image generator.
    2. LLM (Mistral-Small): Used as a text encoder/conditioner for the diffusion process.
    3. VAE (Variational Autoencoder): Used for encoding/decoding image latents.
- Configuration: The script is configured to use CPU offloading and Flash Attention for improved memory and speed efficiency.
- Simple Image Generation: The script executes a single text-to-image generation task and saves the result as an output file.

DEPENDENCIES
------------

This script requires the stable-diffusion-cpp-python package.

Installation:
pip install stable-diffusion-cpp-python

Note: Since stable-diffusion-cpp-python builds the C++ backend from source during installation, you may need a working C++ compiler (like Visual Studio Build Tools on Windows or cmake/make on Linux/macOS) and, optionally, the CUDA toolkit for GPU acceleration.

MODEL CONFIGURATION
-------------------

The script initializes the StableDiffusion object by specifying local paths to three large model files.

- Parameter: diffusion_model_path
  - Model File: flux2-dev-Q4_K_S.gguf
  - Role: The primary diffusion model for image synthesis. (FLUX.2 Dev is a State-of-the-Art open image generation model.)

- Parameter: llm_path
  - Model File: Mistral-Small-3.2-24B-Instruct-2506-UD-IQ1_S.gguf
  - Role: The large language model responsible for processing the text prompt and generating conditioning vectors.

- Parameter: vae_path
  - Model File: ae.safetensors
  - Role: The Variational Autoencoder, used to transform images between pixel space and latent space.

The configuration parameters are set as follows:

- offload_params_to_cpu=True: Offloads model parameters to system RAM to conserve VRAM, useful for GPUs with limited memory.
- diffusion_flash_attn=True: Enables Flash Attention for the diffusion UNet, which significantly reduces VRAM usage and speeds up computation.

USAGE
-----

### 1. File Preparation

Place the three required model files (.gguf and .safetensors) at the exact paths specified in the Diffusion.py file.

Example paths to update in Diffusion.py:
stable_diffusion = StableDiffusion(
    diffusion_model_path=r"C:\Users\Kagero\Downloads\Compressed\flux2-dev-Q4_K_S.gguf", # <--- UPDATE THIS PATH
    llm_path=r"C:\Users\Kagero\Downloads\Compressed\Mistral-Small-3.2-24B-Instruct-2506-UD-IQ1_S.gguf", # <--- UPDATE THIS PATH
    vae_path=r"C:\Users\Kagero\Downloads\Compressed\ae.safetensors", # <--- UPDATE THIS PATH
    # ...
)

### 2. Execution

Run the script from your terminal:

python Diffusion.py

### 3. Output

The script executes the image generation with the following parameters:

- Prompt: "solar system with all the planets and its sun"
- Sample Steps: 4
- CFG Scale: 0.1

The generated image will be saved to the same directory as the script with the filename: output.png.
