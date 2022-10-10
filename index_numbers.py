import MDAnalysis as mda
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import csv


#### needs to clean up big time

def select(grofile,xtcfile,name,system_size):
    u = mda.Universe(grofile,xtcfile)
    prot = u.select_atoms(name)
    system = u.select_atoms(system_size)
    com = prot.center_of_mass()

    halfz = u.dimensions[2]/2 ## Get the half of the z-dimension
    UP = u.select_atoms('name P and prop z > %f' %halfz)
    LP = u.select_atoms('name P and prop z < %f' %halfz)
    c316 = u.select_atoms('name C316')
    return c316



def make_list(test):
    ls=[]

    for atom in test:
    	ls.append(atom)

    df = pd.DataFrame(ls)
    df.to_csv('list.csv')
    csv_file = 'list.csv'
    txt_file = 'text.txt'
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

    with open('text.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('text.txt', 'w') as fout:
        fout.writelines(data[1:])
    f = open('text.txt','r')
    lines=f.readlines()
    result=[]
    for x in lines:
    	result.append(x.split(' ')[2])
    f.close
    new_result=[]
    for element in result:
    	if ':' in element:
    		no_col = element.replace(':','')
    		new_result.append(no_col)
    # open file in write mode
    with open(r'atoms.txt', 'w') as fp:
        for item in new_result:
            # write each item on a new line
            fp.write(','+item)
        print('Done')
