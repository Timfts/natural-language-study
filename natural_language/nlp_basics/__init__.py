from spacy import load
from spacy.language import Language


""" loading the language model """
nlp: Language = load("en_core_web_sm")

""" Create a document object parsing the text with the model """
doc = nlp(u"Tesla is lookin at buying U.S. startup for $6 million")


""" Document tokens """
for token in doc:
    print(f"{token.text} - {token.pos_} - {token.dep_} - {token.lemma_}")

print("\n")
""" ---- new doc ---- """

doc2 = nlp(u"Tesla isn't looking into startups anymore")

for token in doc2:
    print(f"{token.text} - {token.pos_} - {token.dep_} - {token.lemma_}")
