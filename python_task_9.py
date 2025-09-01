student_marksheet = {
    "Alice":85,
    "Bob":90,
    "Charlie":90,
    "David":85,
    "Eve":85
}
std_name = input("Enter student name: ").capitalize()
if std_name in student_marksheet.keys():
    print(std_name+"'s Marks :", student_marksheet[std_name])
else:
    print("Student not found.")