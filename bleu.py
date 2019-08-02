
from nltk.translate.bleu_score import sentence_bleu
from googletrans import Translator
import nltk

reference = []

# Takes original sentence and guess
base = "I am 11 years old."


guess = u"Tengo 11 años."
candidate = nltk.word_tokenize(guess)

translator = Translator()
true = translator.translate(base, src='en', dest='es')
reference.append(nltk.word_tokenize(true.text))

# sentence_bleu(reference, candidate)
score = sentence_bleu(reference, candidate)

print(reference)
print(candidate)
print("Base: {}".format(base))
print("Guess: {}".format(guess))
print("Reference: {}".format(true.text.encode('utf-8')))


print(score)