'''
Created on Jan 7, 2015

@author: ph
'''
import random
import string
from string import Template
import math
import sys

class Params:
    def __init__(self, N, m, b):
        self.N=N
        self.m=m
        self.b=b
        self.r_start=-N
        self.r_end=N


myDatasetFolder='myDataset/'
dataset_filename_appendix='_samples'
dataset_filename_ext='.txt'
dataset_filename_meta_ext='.meta'
dataset_filename_gnuplot_ext='.gp'


def computeY(x, m, b):
    return m*x+b

def recordMetaData(dataset_filename, params):
    mf= open(myDatasetFolder + dataset_filename + dataset_filename_meta_ext, 'w')
    mf.write("N="+str(params.N)+"\n")
    mf.write("m="+str(params.m)+"\n")
    mf.write("b="+str(params.b)+"\n")
    mf.write("r_start="+str(params.r_start)+"\n")
    mf.write("r_end="+str(params.r_end)+"\n")
    mf.close()


def produceGnuplotFile(dataset_filename, params):
    d = {'dataset_filename': dataset_filename, 'm': params.m, 'b': params.b}
    gpf = open(myDatasetFolder + dataset_filename + dataset_filename_gnuplot_ext, 'w')
    # open the file
    filein = open('gnuplot.template')
    # read it
    src = Template(filein.read())
    # do the substitution
    output = src.substitute(d)
    gpf.write(output)
    gpf.close()



def generateNewDataset(params):
    dataset_filename = str(params.N) + dataset_filename_appendix
    X_set = set([])
    X = Y = 0
    f = open(myDatasetFolder+dataset_filename+dataset_filename_ext, 'w')
    while len(X_set)<params.N:
        pre_X=X
        pre_Y=Y
    
        X = random.randint(params.r_start, params.r_end)
        if X not in X_set and X != pre_X:
            X_set.add(X)
            Y=computeY(X, params.m, params.b)
            Y=Y+random.randint(params.r_start, params.r_end)

            #slope= (Y-pre_Y)/(X-pre_X)
            #print X, Y, slope
    
            f.write(str(X)+","+str(Y)+"\n")
    f.close()

    recordMetaData(dataset_filename, params)
    produceGnuplotFile(dataset_filename, params)

if __name__ == '__main__':
    generateNewDataset(Params(int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))
