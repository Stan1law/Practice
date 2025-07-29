def get_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid Grade!!!")
        except ValueError:
            print("Grade must be number.")


def calculate_grade(grades):
    return sum(grades) / len(grades)


def get_remarks(average):
    if 95 <= average <= 100:
        return "Advanced - Passed"
    elif 90 <= average < 95:
        return "Average - Passed"
    elif 70 <= average < 90:
        return "Below Average - Passed"
    else:
        return "Fail"


def print_result(grade_1, grade_2, grade_3):
    grades = [grade_1, grade_2, grade_3]
    average = calculate_grade(grades)
    remarks = get_remarks(average)
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Remarks: {remarks}")


def main():
    grade_1 = get_grade("Enter your first grade: ")
    grade_2 = get_grade("Enter your second grade: ")
    grade_3 = get_grade("Enter your third grade: ")

    print_result(grade_1, grade_2, grade_3)


if __name__ == "__main__":
    main()


class Student:
    def __init__(self):
        self.grades = []

    def input_grades(self):
        for i in range(1, 4):
            while True:
                try:
                    grade = float(input(f"Enter grade {i}: "))
                    if 0 <= grade <= 100:
                        self.grades.append(grade)
                        break
                    else:
                        print("Invalid Grade!")
                except ValueError:
                    print("Grade must be number.")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def get_remarks(self, average):
        if 95 <= average <= 100:
            return "Advanced - Passed"
        elif 90 <= average < 95:
            return "Average - Passesd"
        elif 70 <= average < 90:
            return "Below Average"
        else:
            return "Fail"

    def print_result(self):
        average = self.calculate_average()
        remarks = self.get_remarks(average)
        print(f"Grades: {self.grades}")
        print(f"Average: {average:.2f}")
        print(f"Remarks: {remarks}")


def main():
    student = Student()
    student.input_grades()
    student.print_result()


if __name__ == "__main__":
    main()


def get_grades():
    grades = []
    for i in range(1, 4):
        while True:
            try:
                grade = float(input(f"Enter grade {i}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Invalid Grade!")
            except ValueError:
                print("Grade must be number")


def get_remarks(average):
    if 95 <= average <= 100:
        return "Advanced - Passed"
    elif 90 <= average < 95:
        return "Average - Passed"
    elif 70 <= average < 90:
        return "Below Average - Passed"
    else:
        return "Fail"


def main():
    grades = get_grades()
    average = sum(grades) / len(grades)
    remarks = get_remarks(average)
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Remarks: {remarks}")


if __name__ == "__main__":
    main()
