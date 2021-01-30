import sys
from sys import argv
import os

def asPath(package):
	path = ""
	for c in package:
		if c != '.':
			path += c
		else:
			path += '\\'
	return path

def compile(file_name,package):
	compilation = False
	print("[INFO]: package \t:{}".format(package))
	print("=======================================")
	for file in os.listdir(asPath(package)):
		if file == "{}.class".format(file_name):
			d = os.system("del {}\\{}.class".format(asPath(package),file_name))
			if d == 0:
				print("[INFO]: deleted \t:{}.class".format(file_name))

	os.system("javac -d . {}.java".format(file_name))

	for file in os.listdir(asPath(package)):
		if file == "{}.class".format(file_name):
			compilation = True
	return compilation


def remove_unc(array):
	new_arr = []

	def checkForNewLineAndSemiColon(string):
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
	file_packge = None
	cur_line = ""
	with open(argv[1]+".java",'r') as unit:
		while True: 
			cur_line = unit.readline()
			if len(cur_line) == 0:
				break
			if cur_line.__contains__("package"):
				package = remove_unc(cur_line.split(" "))
				break;
			print(cur_line)
	compstat = compile(argv[1],package)
	print("=======================================")
	if compstat:
		print("[INFO]: status \t\t:succeed")
		if len(argv) > 2:
			if argv[2] == "autorun":
				print("[INFO]: starting application...")
				print("=======================================")
				if len(argv) == 4:
					if argv[3] == "autoclear":
						os.system("cls") 
				os.system("java {}.{}".format(package,argv[1]))

	else:
		print("[INFO]: status \t\t:failed")
	os.system("pause")
if __name__ == "__main__":
	main()
