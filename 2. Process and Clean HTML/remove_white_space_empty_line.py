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

# write data to test.txt
file = open("test.txt", "w")
for i in range(len(data)):
	file.write(data[i] + "\n")