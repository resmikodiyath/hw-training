# student details
name = "Seenu"
age = 15
marks = [85.5, 90.0, 78.5]


# dictionary to store student details
student={
    "name": "Seenu",
    "age": 15,
    "marks": [85.5, 90.0, 78.5]
}

# print data types of each value
print(type(name))
print(type(age))
print(type(marks))


print(isinstance(student["name"], str))
print(isinstance(student["age"], int))
print(isinstance(student["marks"], list))

# calculate total and average marks
total_marks=sum(marks)
print("total marks:", total_marks)

# calculate average marks
average_marks=total_marks/len(marks)
print("average marks:", average_marks)

# determine pass or fail based on average marks
if average_marks >= 40:
    print("Result:", "Pass")
else:
    print("Result:", "Fail")

# print each mark
for i in marks:
    print(i)
    
# Convert marks list to set
marks_set=set(marks)
print(marks_set)

# Create a tuple of subjects
subjects=("english","physics","chemistry")
print(subjects)
print(type(subjects))
# Add a variable remarks = None and print its type
remarks=None
print(remarks)
print(type(remarks))

# Use a boolean is_passed = True or False and print its type.
is_passed = True
print(is_passed)
print(type(is_passed))
is_passed = False
print(type(is_passed))

# formatted student details
print("==============Student Details==============")
print("name:",name)
print("age:",age)
print("marks:",marks)
print("total marks:",total_marks)
print("average marks:",round(average_marks, 2))
print("result:", "Pass" if average_marks >= 40 else "Fail")
print("remarks:", remarks)
