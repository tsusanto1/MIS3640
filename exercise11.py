# Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
# Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.

#a
def abc(words):
    f = open(words,"r")
    d = {}
    for i in f:
        d[i[:-1]] = 0
    return d
d = abc('words.txt')
print(d)
print(len(d))

#b

def has_duplicates(lista):
    dicto = {}
    for i in lista:
        if i not in dicto:
            dicto[i] = 1
        else:
            dicto[i] += 1
    val = dicto.values()
    for i in val:
        if i > 1:
            return True
    return False

lista = ("a", "b", "c", "b")
listb = ("a", "b", "c", "d")
print(has_duplicates(lista))
print(has_duplicates(listb))