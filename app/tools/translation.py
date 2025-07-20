from deep_translator import GoogleTranslator
from langdetect import detect
import logging



class MultilingualTranslator:
    def __init__(self):
        self.supported_lang = ['en', 'ur', 'hi', 'es']


    def detect_lang(self, text : str) -> str:
        try:
            logging.info('Detecting the language')
            return detect(text)
        
        except Exception:
            return 'en'
        

    
    def translate_to_eng(self, text: str, source_lang: str) -> str:
        try:
            logging.info('Translating the language to english')

            if source_lang == 'en':
                return text
            return GoogleTranslator(source=source_lang, target='en').translate(text)
        
        except Exception as e:
            logging.error(f'An error occurred during translation {str(e)}')



    def translate_from_eng(self, text: str, target_lang: str) -> str:
        try:
            logging.info('Translating the language to english')

            if target_lang == 'en':
                return text
            return GoogleTranslator(source='en', target=target_lang).translate(text)
        
        except Exception as e:
            logging.error(f'An error occurred during translation : {str(e)}')



    def process_input(self, text: str) -> tuple[str, str]:
        try:
            logging.info('Processing input data')

            lang = self.detect_lang(text)
            translated = self.translate_to_eng(text, lang)
            return translated, lang
        
        except Exception as e:
            logging.error(f'An error occurred in process input : {str(e)}')



    def process_output(self, text: str, lang: str) -> str:
        try:
            logging.info('Processing output')

            return self.translate_from_eng(text, lang)
        
        except Exception as e:
            logging.error(f'An error occurred : {str(e)}')