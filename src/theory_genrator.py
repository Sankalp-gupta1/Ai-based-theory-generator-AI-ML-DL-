from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize GPT2 model and tokenizer
model_name = "gpt2"  # You can use "gpt-3.5-turbo" for better results if available
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Encode and generate text based on prompt
def generate_theory(prompt, max_length=600):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate theory with the model
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.95, top_k=60, temperature=0.7)

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Function to generate theory on a specific topic
def generate_physics_theory(topic):
    prompt = f"Generate a scientific theory about {topic}."
    theory = generate_theory(prompt)
    return theory

def main():
    print("📚 AI Theory Generator - Start!")
    topic = input("Enter a topic for the theory (e.g., 'quantum mechanics', 'thermodynamics'): ")
    theory = generate_physics_theory(topic)
    print("\nGenerated Theory:")
    print(theory)

if __name__ == "__main__":
    main()



