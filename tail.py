""" This is a more efficient version, since it does not read the entire
file
"""
"""I do not know how is the original author of this code, I copy then modify it for my usage"""
import sys
import os

def tail2():
	if len(sys.argv) == 1:
		print('Usage: tail filename number_of_line')
		sys.exit(1)
	fname = sys.argv[1]	
	bufsize = 8192
	if len(sys.argv) == 2:
		lines = 10
	else:
		lines = int(sys.argv[2])	
	fsize = os.stat(fname).st_size
	 
	iter = 0
	with open(sys.argv[1]) as f:
		if bufsize > fsize:
			bufsize = fsize-1
		data = []
		while True:
			iter +=1
			f.seek(fsize-bufsize*iter)
			data.extend(f.readlines())
			if len(data) >= lines or f.tell() == 0:
				print(''.join(data[-lines:]))
				break

def head():
	if len(sys.argv) == 1:
		print('Usage: head filename number_of_line')
		sys.exit(1)
	fname = sys.argv[1]	
	bufsize = 8192
	if len(sys.argv) == 2:
		lines = 10
	else:
		lines = int(sys.argv[2])	
	fsize = os.stat(fname).st_size	 
	iter = 0
	with open(sys.argv[1]) as f:		
		data = ''
		while True:
			iter +=1
			#f.seek(fsize-bufsize*iter)
			#data.extend(f.readline())
			data = data + f.readline()
			if iter >= lines or f.tell() == 0:
				print(data)
				break
				
if __name__=='__main__':
	head()