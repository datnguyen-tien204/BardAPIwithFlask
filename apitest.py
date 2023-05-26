from flask import Flask, request, jsonify
import os
from googletrans import Translator
import bardapi

app = Flask(__name__)


@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        os.environ['_BARD_API_KEY'] = "Wgia2rCHhIRVedZnzFDiWOTC_fJsyh4y9rl_42oytOsvzVDAbCE5t9AbmCqNbytFzssV8w."
        input_text = request.form['question']

        translator2 = Translator()
        translated_content2 = translator2.translate(input_text, src='vi', dest='en').text

        response = bardapi.core.Bard().get_answer(translated_content2)
        request_data = {
            'content': response['content'],
            'conversation_id': response['conversation_id'],
            'response_id': response['response_id'],
            'factualityQueries': response['factualityQueries'],
            'textQuery': response['textQuery'],
            'choices': response['choices']
        }

        translator = Translator()
        translated_content = translator.translate(request_data['content'], src='en', dest='vi').text

        return translated_content
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
