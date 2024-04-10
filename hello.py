# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from evaluate import load
import evaluate


# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#
# tokenizer1 = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
# model1 = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")

from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

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


@app.route('/roguescore', methods=['GET'])
def rogue():
    rouge = evaluate.load('rouge')
    candidates = ["Summarization is cool", "I love Machine Learning", "Good night"]

    references = [["Summarization is beneficial and cool", "Summarization saves time"],
                  ["People are getting used to Machine Learning", "I think i love Machine Learning"],
                  ["Good night everyone!", "Night!"]
                  ]
    results = rouge.compute(predictions=candidates, references=references)
    print(results)
    return results

@app.route('/home/summary', methods=['GET'])
def disp():
    data = request.args.get('data')
    sequence = (data)
    summary = summarizer(sequence, max_length=1000, min_length=100, do_sample=False)

    print(summary)
    return summary


# driver function
if __name__ == '__main__':
    # Run Flask app using Gunicorn
    app.run(host='0.0.0.0', port=5000)
