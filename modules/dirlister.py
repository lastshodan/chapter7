import os

def run(**args):
	print "[*] in dirlister module"
	files = os.lisdir(".")
	
	return str(files)