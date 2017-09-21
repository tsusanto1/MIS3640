def fibbo(n):
    if n <= 0:
        print("Wrong input")
        return -1
    elif n <= 2:
        return 1
    else:
        return fibbo(n-2) + fibbo(n-1)

print(fibbo(8))