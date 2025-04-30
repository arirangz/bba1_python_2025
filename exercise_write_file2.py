def add_marks():
    with open("user_marks.txt", "a") as file:
        while True:
            mark = input("Enter a mark (press Enter to stop): ")
            if mark == "":
                break
            file.write(mark + "\n")
    print("Marks saved to user_marks.txt")

def display_average():
    total = 0
    count = 0
    with open("user_marks.txt", "r") as file:
        for line in file:
            mark = float(line.strip())
            total += mark
            count += 1
    average = round(total/count, 2)
    print("The average is", average)

def display_menu():
    while True:
        print("Menu:")
        print("Add new marks - press 1")
        print("Display average - press 2")
        print("To exit press 3")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_marks()
        elif choice == "2":
            display_average()
        elif choice == "3":
            break

if __name__ == "__main__":
    display_menu()