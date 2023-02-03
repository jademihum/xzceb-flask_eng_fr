''' This section will add two functions englishToFrench and frenchToenglish '''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='version',
    authenticator=authenticator
)

language_translator.set_service_url('url')
#language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def englishToFrench(english_text):
    '''
    This function converts English to French
    '''
    #write the code here
    #text='Hello, how are you today?'
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text.get['translations'][0]['translation']

def frenchToEnglish(french_text):
    '''
    This function converts French to English
    '''
    #write the code here
    #text='Bonjour?'
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text.get['translations'][0]['translation']
    