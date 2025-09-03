num=int(input("Enter the number:"))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
print(f"sum of digits is {sum}")
