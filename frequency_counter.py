import string
text = "Hello world! Hello everyone. Welcome to the world of Python."
new_text = text.translate(str.maketrans(" "," ", string.punctuation))
txt = list(new_text.lower().split())
text_dict = dict()
for item in txt:
    text_dict.update({item: txt.count(item)})
print(text_dict)