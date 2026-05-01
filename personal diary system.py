try:
    with open("diary.txt", "x") as file:
        file.write("This is my personal diary entry for today.\n")
except FileExistsError:
    print("Diary entry already exists. Appending to the existing diary.")

while True:
    print("\nPersonal Diary System")
    print("1. Add a new diary entry")
    print("2. View diary entries")
    print("3. count all lines in the diary")
    print("4. delete the diary")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        entry = input("Enter your diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
        print("Diary entry added successfully.")
    elif choice == '2':
        with open("diary.txt", "r") as file:
            entries = file.read()
            print("\nDiary Entries:\n")
            print(entries)
    elif choice == '3':        
        with open("diary.txt", "r") as file:
            lines = file.readlines()
            print(f"Total number of lines in the diary: {len(lines)}")
    elif choice == '4':
        with open("diary.txt", "w") as file:
            file.write("")
        print("Diary has been deleted.")
    elif choice == '5':
        print("Exiting the Personal Diary System. Goodbye!")
        break