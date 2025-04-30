with open("user_marks.txt", "w") as file:
    while True:
        mark = input("Enter a mark (press Enter to stop): ")
        if mark == "":
            break
        file.write(mark + "\n")

print("Marks saved to user_marks.txt")