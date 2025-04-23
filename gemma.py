import os
import random
from llama_cpp import Llama

MODEL_PATH = "/assistant/gemma-2-9b.Q4_K_M.gguf"
PROMPT_FILE = "assistant/prompts" 

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,   # adjust based on your Pi 5 performance
    n_batch=32,
    verbose=True
)

def load_random_prompt(prompt_file):
    with open(prompt_file, 'r') as f:
        prompts = [line.strip() for line in f if line.strip()]
    return random.choice(prompts)

# Run model with prompt
def run_gemma(prompt_file):
    user_prompt = load_random_prompt(prompt_file)
    full_prompt = f"[INST] {user_prompt} [/INST]"

    print("🧠 Prompting Gemma with:")
    print(user_prompt)

    output = llm(full_prompt, max_tokens=150, temperature=0.7, top_p=0.9, stop=["</s>"])
    response = output["choices"][0]["text"].strip()
    return response

# Example call
if __name__ == "__main__":
    response = run_gemma(PROMPT_FILE)
    print("🤖 Gemma response:", response)
