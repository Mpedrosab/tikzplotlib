#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pylab import *
import numpy

# =============================================================================
def basic_sin():
        t = arange( 0.0, 2.0, 0.01 )
        s = sin( 2*pi*t )
        plot( t, s, ":" )

        xlabel("time(s)")
        ylabel("Voltage (mV)")
        title("Easier than easy $\\frac{1}{2}$")
        grid( True )

        return "Simple $\sin$ plot with some labels"
# =============================================================================
def subplots():
        def f(t):
            s1 = numpy.cos(2*numpy.pi*t)
            e1 = numpy.exp(-t)
            return numpy.multiply(s1,e1)

        t1 = numpy.arange(0.0, 5.0, 0.1)
        t2 = numpy.arange(0.0, 5.0, 0.02)
        t3 = numpy.arange(0.0, 2.0, 0.01)

        subplot(211)
        l = plot(t1, f(t1), 'bo', t2, f(t2), 'k--', markerfacecolor='green')
        grid(True)
        title('A tale of 2 subplots')
        ylabel('Damped oscillation')

        subplot(212)
        plot(t3, numpy.cos(2*numpy.pi*t3), 'r.')
        grid(True)
        xlabel('time (s)')
        ylabel('Undamped')

        return "Two subplots on top of each other"
# =============================================================================
def image_plot():
    try:
        import Image
    except ImportError, exc:
        raise SystemExit("PIL must be installed to run this example")

    lena = Image.open('lena.png')
    dpi = rcParams['figure.dpi']
    figsize = lena.size[0]/dpi, lena.size[1]/dpi

    figure(figsize=figsize)
    ax = axes([0,0,1,1], frameon=False)
    ax.set_axis_off()
    im = imshow(lena, origin='lower')

    colorbar()

    return "An \\texttt{imshow} plot"
# =============================================================================
def subplot_plot():
        def f(t):
            s1 = cos(2*pi*t)
            e1 = exp(-t)
            return multiply(s1,e1)

        t1 = arange(0.0, 5.0, 0.1)
        t2 = arange(0.0, 5.0, 0.02)
        t3 = arange(0.0, 2.0, 0.01)

        subplot(211)
        l = plot(t1, f(t1), 'bo', t2, f(t2), 'k--', markerfacecolor='green')
        grid(True)
        title('A tale of 2 subplots')
        ylabel('Damped oscillation')

        subplot(212)
        plot(t3, cos(2*pi*t3), 'r.')
        grid(True)
        xlabel('time (s)')
        ylabel('Undamped')

        return "Two subplots on top of each other"
# =============================================================================
def noise():
    import matplotlib.pyplot as plt
    import numpy as np

    from numpy.random import randn

    # Make plot with vertical (default) colorbar
    fig = plt.figure()
    ax = fig.add_subplot(111)

    data = np.clip(randn(250, 250), -1, 1)

    cax = ax.imshow(data, interpolation='nearest')
    ax.set_title('Gaussian noise with vertical colorbar')

    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
    cbar.ax.set_yticklabels(['< -1', '0', '> 1'])# vertically oriented colorbar

    # Make plot with horizontal colorbar
    fig = plt.figure()
    ax = fig.add_subplot(111)

    data = np.clip(randn(250, 250), -1, 1)

    cax = ax.imshow(data, interpolation='nearest')
    ax.set_title('Gaussian noise with horizontal colorbar')

    cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
    cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])# horizontal colorbar

    return "Noise with a color bar"
# =============================================================================
def patches():

    from matplotlib.patches import Circle, Wedge, Polygon
    from matplotlib.collections import PatchCollection

    fig=figure()
    ax=fig.add_subplot(111)

    resolution = 50 # the number of vertices
    N = 3
    x       = rand(N)
    y       = rand(N)
    radii   = 0.1*rand(N)
    patches = []
    for x1,y1,r in zip(x, y, radii):
        circle = Circle((x1,y1), r)
        patches.append(circle)

    x       = rand(N)
    y       = rand(N)
    radii   = 0.1*rand(N)
    theta1  = 360.0*rand(N)
    theta2  = 360.0*rand(N)
    for x1,y1,r,t1,t2 in zip(x, y, radii, theta1, theta2):
        wedge = Wedge((x1,y1), r, t1, t2)
        patches.append(wedge)

    # Some limiting conditions on Wedge
    patches += [
        Wedge((.3,.7), .1, 0, 360),             # Full circle
        Wedge((.7,.8), .2, 0, 360, width=0.05), # Full ring
        Wedge((.8,.3), .2, 0, 45),              # Full sector
        Wedge((.8,.3), .2, 45, 90, width=0.10), # Ring sector
    ]

    for i in range(N):
        polygon = Polygon(rand(N,2), True)
        patches.append(polygon)

    colors = 100*rand(len(patches))
    p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
    p.set_array(array(colors))
    ax.add_collection(p)
    colorbar(p)

    return "Some patches and a color bar"
# =============================================================================
if __name__ == 'main':
    patches()
    show()
# =============================================================================