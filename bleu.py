from nltk.translate.bleu_score import sentence_bleu
from googletrans import Translator
import nltk

# Takes original sentence and guess
base = "It is so lovely to meet you!"
base_tok = nltk.word_tokenize(base)
guess = "Es tan lindo conocerte!"
guess_tok = nltk.word_tokenize(guess)

translator = Translator()

reference = [['this', 'is', 'a', 'test'], ['this', 'is' 'test']]
candidate = ['this', 'is', 'a', 'test']

score = sentence_bleu(reference, candidate)

print(score)