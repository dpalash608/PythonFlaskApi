from flask import Flask, request
import os
import google.generativeai as genai
from flask_cors import CORS


app = Flask(__name__)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

CORS(app)  # This will enable CORS for all routes


@app.route('/summary', methods=['GET'])
def summary():
    data = request.args.get('data')
    response = model.generate_content(
        "summarize this html content in paragraph " + data)
    return response.text


@app.route('/translator', methods=['GET'])
def translator():
    data = request.args.get('data')
    language = request.args.get('language')
    response = model.generate_content(
        "translate this html content" + data + " to " + language)
    return response.text


if __name__ == '__main__':
    # Run Flask app using Gunicorn
    app.run(host='0.0.0.0', port=5000)
