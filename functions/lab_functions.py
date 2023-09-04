import scipy.io
import numpy as np
import functools
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def sinegen(fs, fsig, Nsamp):
    tsamp = 1/fs
    t = np.arange(0, Nsamp*tsamp, tsamp)
    y = np.sin(2*np.pi*fsig*t)
    return t, y


def cosgen(fs, fsig, Nsamp):
    tsamp = 1/fs
    t = np.arange(0, Nsamp*tsamp, tsamp)
    y = np.cos(2*np.pi*fsig*t)
    return t, y

def plot_signal(*args, title='', xlabel='', ylabel='', func='plot', **kwargs):
    fig, ax = plt.subplots()

    eval('ax.'+func+'(*args, **kwargs)')

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.grid()

    plt.tight_layout()
    return plt

def plot_spec(*args, title='', dB=False, func='plot'):
    
    if len(args)==1:
        x=args[0]
    else:
        f_step=args[0]
        x=args[1]
    
    mag = np.real(np.sqrt(x * np.conj(x)))
    phase = np.arctan2(np.imag(x), np.real(x))
    phase = np.unwrap(phase)
    
    fig, axs = plt.subplots(2, 1)
    
    mag_ylabel = 'Magnitude [dB]'
    xlabel='Frequency [Hz]'
    
    if dB is True:
        mag = 20*np.log10(mag)
        mag_ylabel = 'Magnitude [dB]'
    
    if len(args)==1:
        xlabel='Frequency [sample no.]'
        eval('axs[0].'+func+'(mag)')
        axs[1].plot(phase)
    else:
        eval('axs[0].'+func+'(f_step, mag)')
        axs[1].plot(f_step, phase)
        
    axs[0].set(xlabel=xlabel, ylabel=mag_ylabel, title=title)
    axs[1].set(xlabel=xlabel, ylabel='Phase [radians] ')
    axs[0].grid()
    axs[1].grid()
    fig.tight_layout()
    
    return plt


def plot_spec_peaks(*args, **kwargs):

    if len(args)==1:
        x=args[0]
    else:
        f_step=args[0]
        x=args[1]

    mag = np.real(np.sqrt(x * np.conj(x)))
        
    plt = plot_spec(*args, **kwargs)
        
    # Find peaks
    peaks = find_peaks(mag, height=1, threshold=1, distance=1)
    height = peaks[1]['peak_heights']  # List containing the height of the peaks
    peak_pos = [f_step[i] for i in peaks[0]]  # List containing the positions of the peaks  

    # Plot peaks
    axs = plt.gcf().get_axes()
    axs[0].scatter(peak_pos, height, color='r', s=10, marker='D', label='maxima', zorder=4)

    print('Peaks: ')
    for i in peak_pos:
        print("%.1f" % i, end='\n')
        
    return plt


def load(file, var):
    y = scipy.io.loadmat(file)
    y = y[var].flatten()
    return y
