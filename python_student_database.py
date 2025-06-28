students = [
    {"name": "Aman", "marks": 89},
    {"name": "Harshik", "marks": 95},
    {"name": "Sara", "marks": 72},
    {"name": "Neha", "marks": 67},
    {"name": "Zara", "marks": 92}
]
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

while True:
    print(f"\n📝 Student Database")
    print("\n1. View Student Info")
    print("2. Update")
    print("3. Short Students")
    print("4. Search Student")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        for info in students:
            print(f"Name: {info['name']} ➝ Marks: {info['marks']} ➝ Grade: {get_grade(info['marks'])}")

    elif choice == 2:
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
            print(f"Name: {info['name']} ➝ Marks: {info['marks']} ➝ Grade: {get_grade(info['marks'])}")

    elif choice == 3:
        shorting = int(input("\nDo you want to filter students by marks [1] or you want to sort them in descending order [2]?: "))
        if shorting == 1:
            shorting_marks = int(input("Enter the minimum marks to filter: "))
            found = False

            print(f"\nStudents with marks more than {shorting_marks}:")
            for info in students:
                if info['marks'] >= shorting_marks:
                    print(f"Name: {info['name']} ➝ Marks: {info['marks']} ➝ Grade: {get_grade(info['marks'])}")
                    found = True

            if not found:
                print(f"No students have marks above {shorting_marks}.")

        elif shorting == 2:
            shorted_students = sorted(students, key=lambda item: item["marks"], reverse=True)
            for student in shorted_students:
                print(f"{student['name']} ➝ {student['marks']} ➝ Grade: {get_grade(student['marks'])}")

    elif choice == 4:
        search_name = input("Enter the student's name to search: ").lower()
        found = False

        for student in students:
            if student['name'].lower() == search_name:
                print(f"\nFound: {student['name']} ➝ {student['marks']} marks ➝ Grade: {get_grade(student['marks'])}")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 5:
        print("Exiting Student Database. See you!")
        break

    else:
        print("Invalid choice. Please select from the menu.")
