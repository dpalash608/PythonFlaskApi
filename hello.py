# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer1 = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
model1 = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")

# creating a Flask app
app = Flask(__name__)


# run using flask --app hello --debug run

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})


@app.route('/home/summary', methods=['GET'])
def disp():
    data = request.get_json().get("data")
    sequence = (data)
    inputs = tokenizer1.encode(sequence, return_tensors='pt', max_length=512, truncation=True)
    output = model1.generate(inputs, min_length=20, max_length=50)
    summary = tokenizer1.decode(output[0])
    print(summary)
    return summary

# driver function
if __name__ == '__main__':
    # Run Flask app using Gunicorn
    app.run(host='0.0.0.0', port=5000)
