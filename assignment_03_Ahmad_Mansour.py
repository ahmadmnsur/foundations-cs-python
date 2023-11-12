def get_student_by_id(student_data, student_id):
    for student in student_data:
        if student["ID"] == student_id:
            return student
    return None

def get_all_students(student_data):
    return student_data

def get_students_by_major(student_data, major):
    students_in_major = [student for student in student_data if student["Major"] == major]
    return students_in_major

def add_student(student_data, name, age, major, gpa):
    student_id = len(student_data) + 1
    new_student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Major": major,
        "GPA": gpa
    }
    student_data.append(new_student)
    return new_student

def find_common_majors(student_data1, student_data2):
    majors1 = {student["Major"] for student in student_data1}
    majors2 = {student["Major"] for student in student_data2}
    common_majors = majors1.intersection(majors2)
    return common_majors

def delete_student(student_data, student_id):
    for student in student_data:
        if student["ID"] == student_id:
            student_data.remove(student)
            return True
    return False

def calculate_average_gpa(student_data):
    if not student_data:
        return 0.0
    total_gpa = sum(student["GPA"] for student in student_data)
    average_gpa = total_gpa / len(student_data)
    return average_gpa

def get_top_performers(student_data, num_students):

    student_data.sort(key=lambda student: student["GPA"], reverse=True)


    top_performers = []

    
    for student in student_data[:num_students]:
        top_performers.append(student["Name"])

    return top_performers


def display_menu():
    print("1. Get Student by ID")
    print("2. Get All Students")
    print("3. Get Students by Major")
    print("4. Add Student")
    print("5. Find Common Majors")
    print("6. Delete Student")
    print("7. Calculate Average GPA")
    print("8. Get Top Performers")
    print("9. Exit")

def main():
    student_ = {}
    student_data=[]
    number_student=int(input("enter how many  number student do you want to add "))
    for i in range(number_student):
        student_[i]={"ID":int(input("enter Id: ")),"Name": input("enter name: "),"Age": int(input("enter age: ")), "Major": input("enter major :"),"GPA": eval(input("enter GPA: "))}
        student_data+=[student_[i]]
                             

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            student_id = int(input("Enter student ID: "))
            student = get_student_by_id(student_data, student_id)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == 2:
            students = get_all_students(student_data)
            for student in students:
                print(student)

        elif choice == 3:
            major = input("Enter major: ")
            students = get_students_by_major(student_data, major)
            if students:
                for student in students:
                    print(student)
            else:
                print("No students in the specified major.")

        elif choice == 4:
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            major = input("Enter student's major: ")
            gpa = float(input("Enter student's GPA: "))
            new_student = add_student(student_data, name, age, major, gpa)
            print("Student added:", new_student)

        elif choice == 5:
            
            common_majors = find_common_majors(student_data, student_data)
            print("Common majors:", common_majors)

        elif choice == 6:
            student_id = int(input("Enter student ID to delete: "))
            if delete_student(student_data, student_id):
                print("Student deleted.")
            else:
                print("Student not found.")

        elif choice == 7:
            average_gpa = calculate_average_gpa(student_data)
            print("Average GPA of all students:", average_gpa)

        elif choice == 8:
            num_students = int(input("Enter the number of top performers to retrieve: "))
            top_performers = get_top_performers(student_data, num_students)
            print("Top performers:", top_performers)

        elif choice == 9:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

main()


