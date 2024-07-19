from deep_translator import GoogleTranslator




translated = GoogleTranslator(source='spanish', target='english').translate(input())

print(translated)