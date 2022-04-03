from translate import Translator


first = input("In what languaqe? ")
second = input("In what language should it be translated?")

translator= Translator(from_lang= first ,to_lang= second)

user = input("Enter your text: ")
translation = translator.translate(user)
print(translation)


# Guten Morgen --> good morning
