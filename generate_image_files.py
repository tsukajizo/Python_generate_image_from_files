#!/usr/bin/env python

import os
import glob


def get_filepath(rootpath,term):
    file_list = []
    for root,dir,files in os.walk(rootpath):
        for fname in glob.glob(os.path.join(root,term)):
            file_list.append(fname)
    return file_list


def load_files(file_list):
    file_set = {}
    for filepath in file_list:
        fname = filepath[filepath.rfind("/")+1:len(filepath)]
        f = open(filepath,"r")
        file_set.update({fname:f})
    return file_set

def close_files(file_set):
    for f in file_set.values():
        f.close()
        

def get_line_number_with_term(file_set,terms):
    line_set = {}
    for name,f in file_set.items():
        line_number = []
        count = 0
        for line in f:
            if(line.find(terms) != -1):
                line_number.append(count)
            count+=1
        line_set.update({name:line_number})
    return line_set
    
if __name__ == '__main__':
    curdir = os.getcwd()
    extention =( "*." + raw_input("[ Enter extention ]:") )
    pathList = get_filepath(curdir,extention)
    fileset = load_files(pathList)
    terms = raw_input("[ Enter terms ]:")
    lineSet = get_line_number_with_term(fileset,terms)
    close_files(fileset)
    print lineSet
