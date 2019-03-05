import os
#
dirFiles = os.listdir("C:\\Users\\rsingh\\Downloads")
count = 1
for file in os.listdir("C:\\Users\\rsingh\\Downloads"):
	if file[:9] == dirFiles[count][:9]:
		print("duplicate file found: {}".format(file))
		os.remove("C:\\Users\\rsingh\\Downloads\\"+file)
	else:
		# print("unique file {}".format(file))
		pass
	if count == len(dirFiles)-1:
		break
	else:
		count+=1

