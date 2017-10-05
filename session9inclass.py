
#Exercise 2
# def is_abecedarian(word):
#     if len(word) <= 1:
#         return True
#     elif word[0] > word[1]:
#         return False
#     else:
#         return is_abecedarian(word[1:])

# print(is_abecedarian("abcdefg"))
# print(is_abecedarian("bacd"))

#Exercise 3
def is_abecedarian(word):
    counter = 1
    while counter < len(word):
        if word[counter] < word[counter-1]:
            return False
        counter += 1
    return True
print(is_abecedarian("abcdefg"))
print(is_abecedarian("bacd"))
