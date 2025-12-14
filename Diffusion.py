from stable_diffusion_cpp import StableDiffusion

stable_diffusion = StableDiffusion(
    diffusion_model_path=r"C:\Users\Kagero\Downloads\Compressed\flux2-dev-Q4_K_S.gguf",
    llm_path=r"C:\Users\Kagero\Downloads\Compressed\Mistral-Small-3.2-24B-Instruct-2506-UD-IQ1_S.gguf",
    vae_path=r"C:\Users\Kagero\Downloads\Compressed\ae.safetensors",
    offload_params_to_cpu=True,
    diffusion_flash_attn=True,
)

output = stable_diffusion.generate_image(
    prompt="solar system with all the planets and its sun",
    sample_steps=4,
    cfg_scale=0.1,
)
output.image.save("output.png")
