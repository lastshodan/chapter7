import os

def run(**args):
	print "[*] in environmental module"
	return str(os.environ)
