import os

dirFiles = os.listdir(os.getcwd())
count = 1
for file in os.listdir(os.getcwd()):
	if file[:12] == dirFiles[count][:12]:
		print("duplicate file found: {}".format(file))
		os.remove(os.path.join(os.getcwd(),file))
	else:
		# print("unique file {}".format(file))
		pass
	if count == len(dirFiles)-1:
		break
	else:
		count+=1
