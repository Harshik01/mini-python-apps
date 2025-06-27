tasks = []
while True:
    print(f"\n📝 To-Do List Manager")
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")
    
    choice = int(input("\nEnter your choice: "))
    if choice == 5:
        break

    elif choice == 1:
        new_task = input("Add a task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            completed_index = int(input(f"Enter the number of the task you completed: ")) - 1
            tasks[completed_index] += " ✔"
            print("Task marked as completed!")
    
    elif choice == 4:
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        
            delete_index = int(input("Enter the number of the task you want to delete: ")) - 1
            tasks.pop(delete_index)
            print("Task deleted!")
