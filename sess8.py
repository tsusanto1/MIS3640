team = 'New England Patriots'
new_team= team [:12]+ 'Seahawks'
print(new_team)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter: 
            return index
        index = index + 1
    return -1
print(find(team, 'E'))

word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

team = 'New England Patriots'
new_team = team.upper()
print(new_team)

team = 'New England Patriots'
index = team.find('a')
print(index)

#Exercise 4
def printReceipt(items):
    space = 5
    totalPrice = 0
    individualItem = []
    longestL = 0
    for i in items:
        itemPrice = 0
        if longestL < len(i):
            longestL = len(i)
        for j in i:
            itemPrice += ord(j) - 96
        totalPrice += itemPrice
        itemPrice = '{0:.2f}'.format(itemPrice)
        individualItem.append(itemPrice)
    totalPrice = '{0:.2f}'.format(totalPrice)
    for i in range(len(items)):
        print(items[i])
        for j in range(0,space+longestL-len(items[i])):
            print(" ")
        print("$" + individualItem[i] + "\n")
    for i in range(space+5+longestL):
        print(" ")
    print("\nTotal")
    for i in range(space+longestL-5):
        print(" ")
    print(totalPrice)

shoppingCart = ["bananas","rice","paprika","potato chips"]
printReceipt(shoppingCart)


