import glob
import sys

script=sys.argv[0]
suffix=sys.argv[1]
assert len(sys.argv) == 2, 'Introduce only the suffix'
assert suffix[0] != '.', 'Please remove the dot "."'

def main():
	"""This script is a version of the $ls command of the Unix shell.
	Usage: $python my_ls.py suffix
	Output: A list of all the .suffix files in the current directory.
	
	Example:
	----------
	$python my_ls.py csv

	 [' inflammation-01.csv',' inflammation-02.csv','Data.csv']

	"""
	x=glob.glob('*.'+suffix)
	print(x)
