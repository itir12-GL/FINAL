try:
    with open("diary.txt", "r") as file:
        file.write("This is my personal diary entry for today.\n")
except FileNotFoundError:
    print("The diary file does not exist. Creating a new one.")