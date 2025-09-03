fruit=input("Enter ur choice.").strip().title()
if fruit=="Orange":
    print(f"{fruit} is 50 per kg")
elif fruit=="Apple":
    print(f"{fruit} is 120 per kg")
elif fruit=="Banana":
    print(f"{fruit} is 20 per dozen")
else:
    print(f"sorry we are out of {fruit}")
