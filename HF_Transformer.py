import json
import os
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
from transformers import BitsAndBytesConfig


class GPT4AllSession:

    def setup_session(self):
        # Specify the path to the saved model directory
        # model_path = os.path.join(self.model_directory, self.model_name)
        login(token="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")
        quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
)

        model =AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2",device_map="auto")
        tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
        tokenizer.pad_token = tokenizer.eos_token


        # Example usage
        text = "Write a short story about a magical adventure in the forest."
        inputs = tokenizer(text, return_tensors="pt", padding=True)  # Add padding
        inputs['input_ids'] = inputs['input_ids'].to('mps')
        
        outputs = model.generate(
        inputs['input_ids'],  # Include encoded input 
        attention_mask=inputs['attention_mask'],  # Include attention mask
        max_length=50, 
        num_return_sequences=1,
        max_new_tokens=100, do_sample=True
        )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print("Generated Text:", generated_text)

if __name__ == '__main__':
    system_template = '''Given a JSON document with an array of products, each identified by a unique 'productId' and containing a 'description', generate an enhanced description for each product.Focus on extracting and summarizing factual attributes such as description, ingredients, color, size, dimensions, brand, and sub-brand names. Avoid using superlatives or expressive language.
Provide the most relevant top keyword for each product. The response should be a JSON array with the same number of products as the input, structured as: [{{'productId': int, 'enhancedDescription': string, 'keyword': string}}, ...]'''
    prompt_template = '''{0}'''
    model_name = 'mistral-7b-instruct-v0.1.Q4_0.gguf'
    x = GPT4AllSession()
    x.setup_session()