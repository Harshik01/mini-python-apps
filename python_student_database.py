students = [
    {"name": "Aman", "marks": 89},
    {"name": "Harshik", "marks": 95},
    {"name": "Sara", "marks": 72}
]

update = input("\nDo you want to update the list? [Y/N]: ").lower()
if update == "y":
    update_what = int(input("What update you want to make? \nAdd new studenrt[1] or Update any student info[2]: "))
    if update_what == 1:
        name_of_student = input("Enter student's name: ")
        marks = int(input("Enter student's marks: "))

        new_student = {"name": name_of_student, "marks": marks}
        students.append(new_student)
        print("\n Student added!")
    
    elif update_what == 2:
        target_name = input("Enter the name of the student to update: ")

        for info in students:
            if info['name'].lower() == target_name.lower():
                new_marks = int(input("Enter the new marks: "))
                info['marks'] = new_marks
                print("Marks updated!")
                break

else:
    print("\nNo update. Showing original list.")

for info in students:
    print(f"Name: {info['name']} ➝ Marks: {info['marks']} ")

shorting = input("\nDo you want to filter students by marks? [Y/N]: ").lower()
if shorting == "y":
    shorting_marks = int(input("Enter the minimum marks to filter: "))
    found = False

    print(f"\n🎯 Students with marks >= {shorting_marks}:")
    for info in students:
        if info['marks'] >= shorting_marks:
            print(f"Name: {info['name']} ➝ Marks: {info['marks']}")
            found = True

    if not found:
        print(f"No students have marks above {shorting_marks}.")