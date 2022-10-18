file = open("raw_data.txt", "r")

# Read first student
data = file.readline()

# make data becomes a list
data  = data.split("\\n")

# remove \r and \t
for i in range(len(data)):
	data[i] = data[i].replace("\\r", "")
	data[i] = data[i].replace("\\t", "")

# remove tags
for i in range(len(data)):
	tags = []
	for j in range(len(data[i])):
		if data[i][j] == "<":
			begin = j
		if data[i][j] == ">":
			end = j
			tags.append(data[i][begin:end+1])

	for tag in tags:
		data[i] = data[i].replace(tag, "")

# remove leading whitespace
for i in range(len(data)):
	data[i] = data[i].strip()

# remove empty line
unempty_lines = []
for i in range(len(data)):
	if data[i] != "":
		unempty_lines.append(data[i])
data = unempty_lines

# choose relevant information
name = data[7]
dob = data[8]
scores = data[9]

# load unicode table
chars = [] # special characters
codes = [] # code of special characters

file = open("unicode.txt", encoding="utf8")
unicode_table = file.read().split("\n")

for code in unicode_table:
	x = code.split(" ")
	chars.append(x[0])
	codes.append(x[1])

# replace special characters in name and scores
for i in range(len(chars)):
	name = name.replace(codes[i], chars[i])
	scores = scores.replace(codes[i], chars[i])

data = [name, dob, scores]
# write data to test.txt
file = open("test.txt", encoding="utf8", mode="w")
for i in range(len(data)):
	file.write(data[i] + "\n")