A = ["abba", "bbaa", "abbaba", "bbaabb"]

for x in A:
    rev = ""
    
    for ch in x:
        rev = ch + rev   # manually reverse
    
    if x == rev:
        print(x, "Palindrome")
    else:
        print(x, " Not Palindrome")