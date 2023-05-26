import bardapi
import os
from googletrans import Translator


while (True):
    os.environ['_BARD_API_KEY'] = "Wgia2rCHhIRVedZnzFDiWOTC_fJsyh4y9rl_42oytOsvzVDAbCE5t9AbmCqNbytFzssV8w."
    input_text = input("Hãy hỏi gì đó : ")
    translator2=Translator()
    translated_content2 = translator2.translate(input_text, src='vi', dest='en').text
    response = bardapi.core.Bard().get_answer(translated_content2)
    request=response

    content = request['content']
    conversation_id = request['conversation_id']
    response_id = request['response_id']
    factuality_queries = request['factualityQueries']
    text_query = request['textQuery']
    choices = request['choices']

    translator = Translator()
    translated_content = translator.translate(content, src='en', dest='vi').text

    print("Nội dung trả về:", translated_content)
    a=input("Có muốn hỏi tiếp không?[Y]/[N]: ")
    if a.islower()=="n":
        break
    else:
        os.system('cls')

