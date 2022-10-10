import argparse
import re
import os
import subprocess
import numpy as np



def com_atoms():


	with open('trajdata/plumed.dat', 'r') as fin:
		data = fin.read().splitlines(True)

	ls=[]
	for stuff in data:
		if stuff.startswith('COM ATOMS'):
			ls.append(stuff)
		print(ls)
	return(ls[1])





def move_atoms(stuff):
	atoms =  open('atoms.txt', 'r')
	data1 = atoms.read()
	data2='COM ATOMS='+data1[1:]+'     LABEL=c2'
	song =  open('trajdata/plumed.dat', 'r')
	data = song.read()
	data = data.replace(stuff, data2)

	with open(r'trajdata/plumed.dat', 'w') as file:
		file.write(data)

	print("Text replaced")



