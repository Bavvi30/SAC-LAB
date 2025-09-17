s = input("enter a string:")
rev = ""
for ch in s:
    rev = ch + rev
    
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")    
