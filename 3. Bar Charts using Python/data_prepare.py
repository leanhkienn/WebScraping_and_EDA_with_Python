# read file
with open("clean_data.csv", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

# remove last student (empty student)
students.pop()

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# split each student in list
for i in range(len(students)):
	students[i] = students[i].split(",")

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

# loop through all students
for s in students:
	# iterate through all subjects
	for i in range(5,16):
		if s[i] == "-1":
			not_take_exam[i-5] += 1

not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]

# convert to percentage
for i in range(0,11):
	not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student, 2)

print(not_take_exam_percentage)
print(subjects)
print(not_take_exam)
