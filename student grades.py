# Create an empty dictionary to store student names and grades
student_grades = {}

while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in student_grades:
            print("Student already exists.")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"{name} added with grade {grade}.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print("Student not found.")

    elif choice == "3":
        if not student_grades:
            print("No student data available.")
        else:
            print("\nStudent Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select a valid option (1-4).")