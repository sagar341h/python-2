students={
    "sagar":92,
    "rohith":85,
    "sudeep":78,
    "neha":88

}
highest=0
name=""
for student,marks in students.items():
    if marks > highest:
        highest = marks
        name=student

print("highest marks:",highest)
print("student name:",name)        