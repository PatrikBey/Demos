import numpy, matplotlib.pyplot as plt, os, pandas


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



# load in test data
Data = pandas.read_csv(os.path.join(os.getcwd(),'Data/Data.txt', sep=','))



# initialize figure size
plt.figure(figsize=[20,10])

# get movement of animal M1
M1 = Data[Data['ID']=='m1']
M1.shape
# (40,3)

colors = numpy.arange(40)

# plot movement of animal M1
plt.subplot(1,2,1)
plt.scatter(M1['RFID1'],M1['RFID2'],c=colors)
plot_plus_maze()
plt.ylim([-1,21])
plt.xlim([-1,21])
plt.title('M1')

# get movement of animal M2
M2 = Data[Data['ID']=='m2']
M2.shape
# (40,3)
colors = numpy.arange(40)

# plot movement of animal M2
plt.subplot(1,2,2)
plt.scatter(M2['RFID1'],M2['RFID2'],c=colors)
plot_plus_maze()
plt.ylim([-1,21])
plt.xlim([-1,21])
plt.title('M2')

# set title of plot
plt.suptitle('Animal movement Elevated Plus Maze')
plt.tight_layout()

# save plot
plt.savefig(os.path.join(os.getcwd(),'/Data/EPM-plot-skript.png'))




