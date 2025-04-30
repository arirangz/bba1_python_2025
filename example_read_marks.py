total = 0
count = 0

with open("john_marks.txt", "r") as file:
    for line in file:
        mark = float(line.strip())
        total += mark
        count += 1

average = round(total/count, 2)

print("John average:", average)