import sys
from sys import argv
import os

# convert the java package string to path
def asPath(package):
	path = ""
	for c in package:
		if c != '.':
			path += c
		else:
			path += '\\'
	return path

def compile(file_name,package):
	# used to determine wether the compilation is a success or not
	# which will be proccessed to decide if the application is runnable or not
	compilation = False
	comwdel = False
	if package:
		print("[INFO]: package \t:{}".format(package))
		
		print("=======================================")
		# before we compile the file we check if the compiled-version of the java program is 
		# already exist or not if it is then we will delete this file, by doing this we can
		# check if the compilation is success by check if the compiled-version of the java file
		# exist after compilation or not, if there is then we can determine that the compilation
		# is a success
		try:
			for file in os.listdir(asPath(package)):
				if file == "{}.class".format(file_name):
					d = os.system("del {}\\{}.class".format(asPath(package),file_name))
					if d == 0:
						print("[INFO]: deleted \t:{}.class".format(file_name))
		except FileNotFoundError:
			print("[INFO]: package {} not found, performing compilation without deleting previous version".format(package))
			print("[INFO]: compiling {}.java...".format(argv[1]))
			os.system("javac -d . {}.java".format(file_name))
			comwdel = True
	else:
		d = os.system("del {}.class".format(file_name))
		if d == 0:
			print("[INFO]: deleted \t:{}.class".format(file_name))
	if not comwdel:
		print("[INFO]: compiling {}.java...".format(argv[1]))
		os.system("javac -d . {}.java".format(file_name))

	# check if the compiled-version of java program is exist or not
	# if exist return True and False otherwise.
	if package:
		for file in os.listdir(asPath(package)):
			if file == "{}.class".format(file_name):
				compilation = True
	else:
		for file in os.listdir("."):
			if file == "{}.class".format(file_name):
				compilation = True
	return compilation


def remove_unc(array):
	"""remove the unnecessary characters in the string list.
		 return new list contains only the package string
	"""
	new_arr = []

	def checkForNewLineAndSemiColon(string):
		"""delete the new-line character and semi-colon from the string"""
		new_string = ""
		for i in string:
			if i != "\n" and i != ";":
				new_string += i
		return new_string

	for i in range(len(array)):
		if array[i] != '' and array[i] != "package":
			new_arr.append(checkForNewLineAndSemiColon(array[i]))

	return new_arr[0]

def main():
	print("=======================================")
	print("[INFO]: file name \t:{}.java".format(argv[1]))
	file_package = None
	cur_line = ""

	# parse the the java file as lines and look for the string 'package'
	# then call the remove_unc to remove unnecessary characters in the line of where the package
	# string found and if not found then the file_package will keep None which will be processed 
	# by the compile function and will used as compilation status
	with open(argv[1]+".java",'r') as unit:
		while True: 
			cur_line = unit.readline()
			if len(cur_line) == 0:
				break
			if cur_line.__contains__("package"):
				file_package = remove_unc(cur_line.split(" "))
				break
	compstat = compile(argv[1],file_package)
	print("=======================================")

	# the launching phase. by checking the status returned by the compile function
	# we can determine wether the program is compiled successfuly or not
	# then we can launch or not launching to program based on the status
	if compstat:
		print("[INFO]: status \t\t:succeed")
		if len(argv) > 2:
			if argv[2] == "autorun":
				print("[INFO]: starting application...")
				print("=======================================")
				if len(argv) == 4:
					if argv[3] == "autoclear":
						os.system("cls")
				if file_package:
					os.system("java {}.{}".format(file_package,argv[1]))
				else:
					os.system("java {}".format(argv[1]))

	else:
		print("[INFO]: status \t\t:failed")
	os.system("pause")
if __name__ == "__main__":
	main()
