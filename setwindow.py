import argparse
import re
import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt



class MakeWindows:

    def read_dist(dist_file):
    
        f = open(dist_file,'r')
        lines = f.readlines()[17:]
        f.close()

        ### now we need to start at line 17 and read down
        out_dict = {}

        for i in range(len(lines)):
        # Split on white-space; grab frame/distance
            columns = lines[i].split()
            num=float(columns[0])
            dist=float(columns[3])
            out_dict[num] = dist
        keys = out_dict.keys()
        sorted(keys)
        out = [(k,out_dict[k]) for k in keys]
        return out



    def get_dist(dist_list, inp_num):
    
        distances = [d[1] for d in dist_list]
        current=0
        sampled=[current]
        while current < len(distances):
    #         print(current,'current')
    ###################### below changes to + sometimes

            targ = distances[current] - inp_num
            
    #         print(targ,'targ')
            on = [abs(targ-d) for d in distances[current:]]
            next_ = on.index(min(on)) + current
            if current == next_:
                break
            else:
                sampled.append(next_)
                current = next_
        return sampled


    def returning(stuff):
        for num in range(len(stuff)):
            return num


    def trjconv(grofile,xtcfile,newgrofile,begin,end):
        myexec = 'gmx'
        args = [myexec,'trjconv',
               '-f', xtcfile,
               '-s', grofile,
               '-o', newgrofile,
               '-b', begin,
               '-dump', end]
        p = subprocess.Popen(args, 
                                 stdin=subprocess.PIPE,
                                 )
        p.stdin.write(b'0\n')
        p.communicate()[0]
        p.stdin.close()
        p.wait()




    def grompp(mdpfile,grofile,topfile,tprfile,ndxfile):
        myexec = 'gmx'
        args = [myexec,'grompp',
               '-f', mdpfile,
               '-c', grofile,
               '-p', topfile,
               '-o', tprfile,
               '-n', ndxfile,
                ]
        p = subprocess.Popen(args, 
                                 stdin=subprocess.PIPE,
                                 )
        p.stdin.write(b'0\n')
        p.communicate()[0]
        p.stdin.close()
        p.wait()
    

    def distance(grofile,xtcfile,ndxfile,xvgfile,select):
        myexec = 'gmx'
        args = [myexec,'distance',
               '-f', xtcfile,
               '-s', grofile,
               '-n', ndxfile,
               '-oxyz', xvgfile,
               '-select', select,
                ]
        p = subprocess.Popen(args, 
                                 stdin=subprocess.PIPE,
                                 )
        p.stdin.write(b'0\n')
        p.communicate()[0]
        p.stdin.close()
        p.wait()
