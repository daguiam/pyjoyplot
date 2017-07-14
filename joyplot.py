#!/usr/bin/env python
""" joyplots using matplotlib
"""

import matplotlib.pylab as plt
import numpy as np
import pandas as  pd

def joyplot(data,
            labels=None,
            overlap=0.5,
            fill=False,
            color=None,
            facecolor=None,
            edgecolor=None,
            alpha=None,
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
    ylabelpoints = np.array(list(reversed(range(totalplots))))
    handles = []
    for i in range(totalplots):
        
        x,y = data[i]
        label = labels[i]
        #print label#,,y
        ystart = ylabelpoints[i]
        y = y*(overlap)+ystart+0.05
        if fill:
            hax = ax.fill_between(x, ystart, y, 
                        interpolate=True)

        else:
            hax = ax.plot(x, y)
        handles.append(hax)
    for hax in handles:
        if color is not None:
                hax.set_color(color)
        if fill:
            if facecolor is not None:
                    hax.set_facecolor(facecolor)
            if edgecolor is not None:
                    hax.set_edgecolor(edgecolor)
        if alpha is not None:
                hax.set_alpha(alpha)

    ax.set_yticks(np.array(ylabelpoints)+0.5)
    ax.set_yticklabels(labels)
    ax.tick_params(axis='both',left=False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
if __name__ == "__main__":

    data = []
    labels = []
    for i in range(10):
        x1 = np.linspace(0,24,100)
        y1 = np.abs(np.random.randn(len(x1)))
        y1 = np.abs(np.random.randn(len(x1)))

        y1 = y1/np.max(y1)
        
        data.append([x1,y1])
        labels.append('Data %d'%(i))
    
    # ETL
    if 1:
        data = []
        labels = []
        df = pd.read_fwf('birthsRR.txt',widths=[4,5,8,12])
        print df
        #df = pd.read_fwf('birthsTR.txt')
        year = '2013'
        yd = df.loc[df['Year']==year]

        
        countries = sorted(list(set(yd['Code'])))
        for code in countries:
            cd = yd.loc[df['Code']==code]
            x = np.array(cd['Age'])
            #x[x=='12-'] = '12'
            #x[x=='55+'] = '55'
            x = x.astype(np.int)
            
            y = np.array(cd['Total']).astype(np.float)
            if code == 'USA':
                print cd
                print 'USA', zip(x,y)
            y = y/np.max(y)

            labels.append(code)
            data.append([x,y])


    #labels = ['Data 1','Data 2']
    #data = [[x1, y1], [x1, y2]]
    joyplot(data, 
            labels=labels, 
            overlap=0.8, 
            fill=True,
            #color='C0',
            facecolor='C0',
            edgecolor='w',
            alpha=1)

    plt.xlabel('Age')
    plt.title('Live births distribution by age in %s'%(year))
    plt.xlim([12,55])

    plt.show()