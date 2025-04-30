total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        number = float(line.strip())
        total += number


print("Total:", total)