from tools.translation import MultilingualTranslator
from tools.google_search import GoogleSearchTool


translator = MultilingualTranslator()
search_tool = GoogleSearchTool()

text_en, lang = translator.process_input("¿Qué es inteligencia artificial?")
result = search_tool.run(text_en)
output = translator.process_output(result, lang)
print(output)
print(lang)