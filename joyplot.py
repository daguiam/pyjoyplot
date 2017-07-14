#!/usr/bin/env python
""" joyplots using matplotlib
"""

import matplotlib.pylab as plt
import numpy as np

def joyplot(data,
            labels=None,
            overlap=0.5,
            fill=False,
            ax=None):
    """ joyplot

    Parameters
    ----------
    data
        List of [[x1,y1],[x2,y],...] data to be plotted
    labels
        Text labels of each data in the list
    overlap
        Overlapping of consecutive plots
    fill: bool
        Fills between base and line

    Returns
    -------
    bool
        True if successful, False otherwise.
    """
    ax = ax or plt.gca()


    data = np.array(data)
    overlap += 1

    # Normalizing ydata
    ydata = data[:,1]
    maxydata = np.max(ydata)
    data[:,1] = ydata/maxydata
    
    
    totalplots = len(data)
    ylabelpoints = list(reversed(range(totalplots)))
    for i in range(totalplots):
        
        x,y = data[i]
        label = labels[i]
        print label#,,y
        ystart = ylabelpoints[i]
        y = y*(overlap)+ystart
        if fill:
            ax.fill_between(x, ystart, y)
        else:
            ax.plot(x, y)
    ax.set_yticks(ylabelpoints)
    ax.set_yticklabels(labels)

if __name__ == "__main__":
    x1 = np.linspace(0,24,100)
    y1 = np.abs(np.random.randn(len(x1)))
    #x2 = np.linspace(0,24,100)
    y2 = np.abs(np.random.randn(len(x1)))
    
    labels = ['Data 1','Data 2']
    data = [[x1, y1], [x1, y2]]
    joyplot(data, labels=labels, overlap=1, fill=True)
    


    plt.show()