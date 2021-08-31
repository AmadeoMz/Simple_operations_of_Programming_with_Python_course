import sys
import numpy as np

def main():
	"""This program open the .csv files specified in the command-line with the NumPy library 
	and compares the number of rows and columns from each file.
	Example:
	----------
	$python rows_columns_comparison.py *.csv
	"""

	script=sys.argv[0]
	filenames = sys.argv[1:]
	assert len(filenames)>=2, 'Please introduce at least two filenames'
	check(filenames)



def check(filenames):
	for file in filenames:
	 data=np.loadtxt(fname=file, delimiter=',')
	 (rows, columns) = data.shape
	 for file_comp in filenames:
	   data_comp=np.loadtxt(fname=file_comp, delimiter=',')
	   (rows_comp, columns_comp) = data_comp.shape
	   assert rows == rows_comp, 'At least one is different:'
	   assert columns == columns_comp, 'At least one is different:'
	print('All the files have the same number of rows and columns', (rows, columns))


if __name__=='__main__':
	main()
