# simple translation test code (using deep_translator documentation)
from deep_translator import GoogleTranslator

text_to_translate = "పుస్తకము యొక్క ముఖ్య భాగములు ఏమిటి?"
target_language_code = "en" 

translator = GoogleTranslator(source='auto', target=target_language_code)
translated_text = translator.translate(text=text_to_translate)

print(f"Original text: {text_to_translate}")
print(f"Translated text (English): {translated_text}")