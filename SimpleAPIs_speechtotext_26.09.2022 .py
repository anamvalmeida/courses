"""
    Speech To Text Below Code

Region: au-syd
APIKEY: 3ThtNSt_oufTloiyDxBlZUPfkLhwEkV3IkdSpLKlblVm
URL: https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/a9c50606-21c2-4d28-98d2-6ab4682f8fff
"""

from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Insert API Key in place of 'YOUR UNIQUE API KEY'
authenticator = IAMAuthenticator('3ThtNSt_oufTloiyDxBlZUPfkLhwEkV3IkdSpLKlblVm') 
service = SpeechToTextV1(authenticator = authenticator)
   
#Insert URL in place of 'API_URL' 
service.set_service_url('https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/a9c50606-21c2-4d28-98d2-6ab4682f8fff')

with open(r'\Users\Ana\Desktop\Courses\AppliedAI_IBM\audio-file.mp3', 'rb') as f:
    res = service.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel').get_result()
# Check the API documentation - https://cloud.ibm.com/apidocs/speech-to-text?code=python#recognize
# Older codes used:
#   res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
# But my code presented the following error: request() got an unexpected keyword argument 'continuous'
# So, 'continuous=True' was eliminated. It now works.

print('Recognize Function Outcome:',res)
print(' ')

text = res['results'][0]['alternatives'][0]['transcript']
print('Speech to Text:',text)
print(' ')

confidence = res['results'][0]['alternatives'][0]['confidence']
print('Confidence:',confidence)

# To export file as '.txt'
with open('audio-file-output.txt', 'w') as out:
    out.writelines(text)
