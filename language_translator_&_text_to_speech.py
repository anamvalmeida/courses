"""
    Language Translator & Text to Speech

Author: Ana M. Almeida
Date: 27.09.2022

Guide: https://github.com/nicknochnack/LanguageTranslationandIdentification/blob/master/Language%20Translation.ipynb
"""

#   Language Translator
print('LANGUAGE TRANSLATOR')
print(' ')
Region= 'eu-gb'
APIKEY_lt = 'UH2BeXZpusMcOvBa4K5jzOGF_kBMsFDBA99BT4W4XmUF'
URL_lt = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/91d6cd36-f373-40c5-875c-29837c066745'
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(APIKEY_lt)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(URL_lt)

text = 'several tornadoes touched down as a line of severe thunderstorms swept through Colorado on Sunday'
print('Original Text:', text)
print(' ')

translation = lt.translate(text, model_id = 'en-de').get_result()
print('Result:',translation)
print(' ')

text = translation['translations'][0]['translation']
print('In German:', text)
print(' ')

# Detection of Language with Confidence Level
language = lt.identify(text).get_result()
print('Language and Confidence:', language)
print(' ')

#   Text to Speech
print('TEXT TO SPEECH')
print(' ')

APIKEY_tts = '0JzRTlOV_ufMf54eKgX_ucndfUMsBX9i_1VJIudnIe29'
URL_tts = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/32916acf-f916-47fd-b3c6-64a73c74635a'
from ibm_watson import TextToSpeechV1

ttsauthenticator = IAMAuthenticator(APIKEY_tts)
tts = TextToSpeechV1(authenticator = ttsauthenticator)
tts.set_service_url(URL_tts)

text='We are sinking! Please send help!'
print('Original Text:',text)
print(' ')

translation = lt.translate(text, model_id='en-it').get_result()
text = translation['translations'][0]['translation']
print('In Italian:',text)
print(' ')

with open('./help.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='it-IT_FrancescaV3Voice').get_result()
    audio_file.write(res.content)
# API documentation - https://cloud.ibm.com/apidocs/text-to-speech#synthesize

