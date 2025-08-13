subjects = int(input("Enter the number of subjects: "))

student_dict = {}

for i in range(subjects):
    subject_name = input(f"Enter the name of subject {i + 1}: ")
    marks = float(input(f"Enter the marks for {subject_name}: "))
    student_dict[subject_name] = marks

print("\n📚 Student Marks Dictionary:")
for subject, marks in student_dict.items():
    print(f"{subject}: {marks}")

marks_list = list(student_dict.values())
total_marks = sum(marks_list)  
average = round(total_marks / len(marks_list), 2)  


print(f"Total Subjects: {len(marks_list)}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average}")

if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"


print(f"🎯 Final Grade: {grade}")
