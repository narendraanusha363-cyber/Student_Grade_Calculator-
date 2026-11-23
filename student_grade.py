def average(marks):
    return sum(marks) / len(marks)
def grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"
def is_pass(marks):
    return all(mark >= 40 for mark in marks)
def main():
    print("STUDENT GRADE CALCULATOR")
    name = input("Student name: ")
    marks = []
    for i in range(1, 4):
        marks.append(float(input(f"Subject {i} marks: ")))
    avg = average(marks)
    print("Name:", name)
    print("Average:", round(avg, 2))
    print("Grade:", grade(avg))
    print("Pass:", is_pass(marks))
if __name__ == "__main__":
    main()