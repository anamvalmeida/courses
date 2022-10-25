"""
    Project:
     - Using the IBM Watson APIs to create two language translators.
     - English to French and English to German. 

Author: Ana M. Almeida
Date: 25.10.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/Instructions_for_Speech_to_Text_and_Language_Translator_API_Keys_v2.pdf
"""

api_lt = 'UH2BeXZpusMcOvBa4K5jzOGF_kBMsFDBA99BT4W4XmUF'
url_lt = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/91d6cd36-f373-40c5-875c-29837c066745'

api_stt = '3ThtNSt_oufTloiyDxBlZUPfkLhwEkV3IkdSpLKlblVm'
url_stt = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/a9c50606-21c2-4d28-98d2-6ab4682f8fff'

from ibm_watson import LanguageTranslatorV3, SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource # Speech To Text
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator_lt = IAMAuthenticator(api_lt)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator = authenticator_lt)
lt.set_service_url(url_lt)

authenticator_stt = IAMAuthenticator(api_stt)
stt = SpeechToTextV1(authenticator = authenticator_stt)
stt.set_service_url(url_stt)

def englishtofrench(text):
    translation = lt.translate(text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    print('Translation en-fr:',french_text)
    return french_text

def englishtogerman(text):
    translation = lt.translate(text, model_id='en-de').get_result()
    german_text = translation['translations'][0]['translation']
    print('Translation en-de:',german_text)
    return german_text

# englishtofrench('Hello!')
