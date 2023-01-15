#!/bin/python
#
# # RUN.py
#
# * Brain Simulation Section
# * Charité Berlin Universitätsmedizin
# * Berlin Institute of Health
#
# ## Author(s)
# * Bey, Patrik, Charité Universitätsmedizin Berlin, Berlin Institute of Health
# 
#
# * last update: 2023.01.15
#
#
# This script creates plots of elevated plus mazes for given animals.
#
#
#

#############################################
#                                           #
#           PREPARE WORKSPACE               #
#                                           #
#############################################

import os, sys, numpy, matplotlib.pyplot as plt, argparse, glob





#############################################
#                                           #
#           HELPER FUNCTIONS                #
#                                           #
#############################################

def get_data(_filename):
    '''
    load data into array
    '''
    import numpy
    return(numpy.genfromtxt(_filename,dtype='str',delimiter = ',', skip_header=1))

def plot_movements(_data, _title=''):
    '''
    plot movement pattern of animal
    '''
    import numpy, matplotlib.pyplot as plt
    colors = numpy.arange(_data.shape[0])
    plt.scatter(_data[:,0], _data[:,1], c = colors)
    plt.xlim([-1,21])
    plt.ylim([-1,21])
    plt.title(_title)

def plot_plus_maze():
    '''
    plot borders of pluz maze
    '''
    import matplotlib.pyplot as plt
    plt.vlines(0,9,11, color = 'black' )
    plt.vlines(20,9,11, color = 'black' )
    plt.vlines(9,0,9, color = 'black' )
    plt.vlines(11,0,9, color = 'black' )
    plt.vlines(9,11,20, color = 'black' )
    plt.vlines(11,11,20, color = 'black' )
    plt.hlines(9,0,9, color = 'black' )
    plt.hlines(9,11,20, color = 'black' )
    plt.hlines(11,0,9, color = 'black' )
    plt.hlines(11,11,20, color = 'black' )
    plt.hlines(20,9,11, color = 'black' )
    plt.hlines(0,9,11, color = 'black' )
    plt.vlines(0,9,11, linewidths = 5, color = 'black' )
    plt.vlines(20,9,11, linewidths = 5, color = 'black' )
    plt.hlines(9,0,5, linewidths = 5, color = 'black' )
    plt.hlines(9,15,20, linewidths = 5, color = 'black' )
    plt.hlines(11,0,5, linewidths = 5, color = 'black' )
    plt.hlines(11,15,20, linewidths = 5, color = 'black' )

def get_animal(_data, _id):
    '''
    get subset of data for given animal
    '''
    import numpy
    return(_data[numpy.where(_data[:,2]==_id),:2].astype(float).reshape(-1,2))

def log_msg( _string):
    '''
    logging function printing date, scriptname & input string to stdout
    '''
    import datetime, os, sys
    print(datetime.date.today().strftime("%a %B %d %H:%M:%S %Z %Y") + " " + str(os.path.basename(sys.argv[0])) + ": " + str(_string))

def init_statusbar(_length):
    '''
    initializing status bar for progress display in terminal
    '''
    import progressbar
    statusbar = progressbar.ProgressBar(maxval=_length, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    return(statusbar)

#############################################
#                                           #
#         PARSE INPUT VARIABLES             #
#                                           #
#############################################


parser = argparse.ArgumentParser(description='Plot animal movement.')
parser.add_argument('--filename', type=str, help='Provide filename', default='/data/Data.txt') 
args = parser.parse_args()


#############################################
#                                           #
#         PERFORM COMPUTATIONS              #
#                                           #
#############################################

log_msg(f'START:    plotting EPM movement for {os.path.basename(args.filename)}')


Data = get_data(args.filename)

Animals = list(numpy.unique(Data[:,2]))

plt.figure(figsize=[20,10])

pb = init_statusbar(len(Animals))
pb.start()

for a in Animals:
    plt.subplot(1,len(Animals),Animals.index(a)+1)
    plot_movements(get_animal(Data,a), _title = a)
    plot_plus_maze()
    pb.update(Animals.index(a)+1)

plt.suptitle(f'Elevated plus maze - {os.path.basename(args.filename)}', fontsize = 20)

plt.tight_layout()

plt.savefig(os.path.join(os.path.dirname(args.filename),'EPM-plot-docker.png'))

log_msg(f'FINISHED:    plotting EPM movement for {os.path.basename(args.filename)}')