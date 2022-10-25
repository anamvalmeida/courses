"""
    Project:
     - Using the IBM Watson APIs to create two language translators.
     - English to French and English to German. 

Author: Ana M. Almeida
Date: 25.10.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/Instructions_for_Speech_to_Text_and_Language_Translator_API_Keys_v2.pdf
"""

# Create a '__init__.py' file in the same folder as the 'project_speechtotext_and_languagetranslator.py' 
import project_speechtotext_and_languagetranslator

project_speechtotext_and_languagetranslator.englishtofrench('hello')
project_speechtotext_and_languagetranslator.englishtogerman('hello')

# Then cmd to test it using pylint
