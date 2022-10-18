file = open("raw_data.txt", "r")

# Read first student
data = file.readline()

# make data becomes a list
data  = data.split("\\n")

# remove \r and \t
for i in range(len(data)):
	data[i] = data[i].replace("\\r", "")
	data[i] = data[i].replace("\\t", "")


# write data to test.txt
file = open("test.txt", "w")
for i in range(len(data)):
	file.write(data[i] + "\n")