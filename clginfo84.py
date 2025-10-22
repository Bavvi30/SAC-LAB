class_info={
   "class_name":"CSE(AI)",
   "semester":3,
   "subject": "SAC LAB"}

students = {
       {"name": "ankitha", "rollno":84},
       {"name": "harshitha", "rollno":74},
       {"name": "thanmayee", "rollno":54}
   }
def display_class_info():
    print("class information:")
    for key, value in class_info.items():
        print(f"{key.capitalize()}:[value]")
def display_student():
    print("\nstudents list:")
    for s in students:
        print(f" Roll no: {s[roll_no]}-name:{s['name']}")

