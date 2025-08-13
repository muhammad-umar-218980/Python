subjects = int(input("Enter the number of subjects: "))

student_dict = {}

for i in range(subjects):
    subject_name = input(f"Enter the name of subject {i + 1}: ")
    marks = float(input(f"Enter the marks for {subject_name}: "))

    print(f"{subject_name}: {marks}")
    student_dict[subject_name] = marks

print("\nStudent Marks Dictionary:")

for subject, marks in student_dict.items():
    print(f"{subject}: {marks}")


marks_list = list(student_dict.values())

subject_count = len(marks_list)
print(f"\nTotal Subjects: {subject_count}")

total_marks = 0

for m in marks_list:
    total_marks = total_marks + m

print(f"\nTotal Marks: {total_marks}")

average = total_marks / subject_count
print(f"\nAverage Marks: {average}")




# Step 5: Grade evaluation
if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"

print(f"\nGrade: {grade}")
