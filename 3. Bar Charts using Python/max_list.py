# read file
with open("clean_data.csv", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# split each student in list
for i in range(len(students)):
	students[i] = students[i].split(",")

# remove last student (empty student)
students.pop()

name = [] # Danh sách các họ
name_count = [] # Số lần lặp của họ

for s in students:
	s_name = s[1].split(" ")
	lastname = s_name[0]
	if lastname not in name:
		name.append(lastname)
		name_count.append(0)
		name_count[name.index(lastname)] += 1
	else:
		name_count[name.index(lastname)] += 1

print(name)
print(name_count)

counted_max_num = [] # Số lần lặp lại các họ từ lớn đến bé

for i in range(len(name)):
	max_number = 0
	for j in range(len(name)):
		if name_count[j] > max_number and name_count[j] not in counted_max_num:
			max_number = name_count[j]

	counted_max_num.append(max_number)

print(counted_max_num)