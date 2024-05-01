from llama_cpp import Llama

# Assuming you have a compatible Llama model file
model_path = "models/Hermes-2-Pro-Mistral-7B.Q2_K.gguf"  
my_aweseome_llama_model = Llama(model_path)

prompt = "This is a prompt"
max_tokens = 100
temperature = 0.3
top_p = 0.1
echo = True
stop = ["Q", "\n"]


# Define the parameters
model_output = my_aweseome_llama_model(
       prompt,
       max_tokens=max_tokens,
       temperature=temperature,
       top_p=top_p,
       echo=echo,
       stop=stop,
   )
final_result = model_output
print(final_result)