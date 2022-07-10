"""AI is creating summary for translator
    Translator module contains function for translatin French and English text
    Returns:
        translated Text: translates text from English to French & vice versa
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']

url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

VERSION = '2018-05-01'

language_translator = LanguageTranslatorV3(authenticator= authenticator, version = VERSION)

language_translator.set_service_url(url)


#Create a function that translates English to French
def english_to_french(english_text):
    """
    AI is creating summary for english_to_french
    Args: english_text (string): English text
    Returns: string in French Language
    """
    if english_text != '':
        translation_response = language_translator.translate(text=english_text, model_id='en-fr')
        translation = translation_response.get_result()
        french_translation = translation['translations'][0]['translation']
        return french_translation
    return ''


#Create a function that translates French to English
def french_to_english(french_text):
    """
    AI is creating summary for french_to_english
    Args: french_text (string): A French text
    Returns: string in English language
    """
    if french_text != '':
        translation_response = language_translator.translate(text=french_text, model_id='fr-en')
        translation = translation_response.get_result()
        english_translation = translation['translations'][0]['translation']
        return english_translation
    return ''
