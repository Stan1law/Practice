import java.util.Scanner;

public class Grading {
    public static double getGrade(Scanner scanner, String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                double grade = Double.parseDouble(scanner.nextLine());
                if (grade >= 0 && grade <= 100) {
                    return grade;
                } else {
                    System.out.println("Invalid Grade!!!");
                }
            } catch (NumberFormatException e) {
                System.out.println("Grade must be number.");
            }
        }
    }

    public static double calculateGrade(double[] grades) {
        double sum = 0;
        for (double grade : grades) {
            sum += grade;
        }
        return sum / grades.length;
    }

    public static String getRemarks(double average) {
        if (average >= 95 && average <= 100) {
            return "Advanced - Passed";
        } else if (average >= 90 && average < 95) {
            return "Average - Passed";
        } else if (average >= 70 && average < 90) {
            return "Below Average - Passed";
        } else {
            return "Fail";
        }
    }

    public static void printResult(double[] grades) {
        double average = calculateGrade(grades);
        String remarks = getRemarks(average);
        System.out.print("Grades: [");
        for (int i = 0; i < grades.length; i++) {
            System.out.print(grades[i]);
            if (i < grades.length - 1)
                System.out.print(", ");
        }
        System.out.println("]");
        System.out.printf("Average: %.2f\n", average);
        System.out.println("Remarks: " + remarks);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double grade1 = getGrade(scanner, "Enter your first grade: ");
        double grade2 = getGrade(scanner, "Enter your second grade: ");
        double grade3 = getGrade(scanner, "Enter your third grade: ");
        double[] grades = { grade1, grade2, grade3 };
        printResult(grades);
        scanner.close();
    }
}

class Student {
    private double[] grades = new double[3];

    public void inputGrades(Scanner scanner) {
        for (int i = 0; i < grades.length; i++) {
            while (true) {
                try {
                    System.out.print("Enter grade " + (i + 1) + ": ");
                    double grade = Double.parseDouble(scanner.nextLine());
                    if (grade >= 0 && grade <= 100) {
                        grades[i] = grade;
                        break;
                    } else {
                        System.out.println("Invalid Grade");
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Grade must be number.");
                }
            }
        }
    }

    public double calculateAverage() {
        double sum = 0;
        for (double grade : grades) {
            sum += grade;
        }
        return sum / grades.length;
    }

    public String getRemarks(double average) {
        if (average >= 95 && average <= 100) {
            return "Advanced - Passed";
        } else if (average >= 90 && average < 95) {
            return "Average - Passed";
        } else if (average >= 70 && average < 90) {
            return "Below Average - Passed";
        } else {
            return "Poor - Failed";
        }
    }

    public void printResult() {
        double average = calculateAverage();
        String remarks = getRemarks(average);
        System.out.print("Grades: [");
        for (int i = 0; i < grades.length; i++) {
            System.out.print(grades[i]);
            if (i < grades.length - 1)
                System.out.print(", ");
        }
        System.out.println("]");
        System.out.printf("Average: %.2f\n", average);
        System.out.println("Remarks: " + remarks);
    }
}

public class Grading {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Student student = new Student();
        student.inputGrades(scanner);
        student.printResult();

    }
}
