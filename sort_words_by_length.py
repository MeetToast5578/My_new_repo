words = ["apple", "banana", "pear", "grape"]
# my_dict = dict()
# sorted_words = list()
new_list = list()
while words:
    shortest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    new_list.append(shortest_word)
    words.remove(shortest_word)
print(new_list)

# for word in words:
#     if len(word) not in my_dict:
#         my_dict[len(word)] = list()
#     my_dict[len(word)].append(word)
# for item in sorted(my_dict):
#     sorted_words.extend(my_dict.get(item))
# print(*sorted_words)