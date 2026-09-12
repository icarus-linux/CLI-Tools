list = []

continueUser = "1"

while continueUser == "1":
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        list.append(task)
    elif choice == "2":
        for task in list:
            print(task)
    elif choice == "3":
        task = input("Enter task to remove: ")
        list.remove(task)
    elif choice == "4":
        continueUser = "0"
    else:
        print("Invalid option")