from flask import Flask, render_template, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Initialize GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate theory
def generate_theory(prompt, max_length=200):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.95, top_k=60, temperature=0.7)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_theory', methods=['POST'])
def generate():
    topic = request.form['topic']
    theory = generate_theory(f"Generate a scientific theory about {topic}")
    return render_template('index.html', theory=theory)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
 