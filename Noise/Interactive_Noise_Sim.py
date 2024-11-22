import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.optimize import curve_fit

rng = np.random.default_rng()

def function_Sine(x,a,c,d):
    return a*np.sin(x+c) + d

def Mod_Depth(signal):
    m_value = (np.max(signal) - np.min(signal)) / (np.max(signal) + np.min(signal))
    return m_value

step_size = np.pi/180
xs = np.arange(0,2*np.pi,step_size)
x_deg = np.degrees(xs)
amp_scaler = 0.5
clean_signal = amp_scaler*np.sin(xs) + amp_scaler

white_noise_scale = 0
shot_noise_scale = 0

def update(val):
    white_noise_scale = slider_white_noise.val
    shot_noise_scale = slider_shot_noise.val
    

    white_noise = np.abs(rng.normal(loc=0,scale=np.std(clean_signal),size=clean_signal.size)) * white_noise_scale
    white_noise_signal = clean_signal + white_noise

    shot_noise = rng.poisson(lam=clean_signal,size=clean_signal.size) * shot_noise_scale
    shot_noise_signal = clean_signal + shot_noise

    full_noisy_signal = clean_signal + white_noise + shot_noise

    popt,pcov = curve_fit(function_Sine,xs,full_noisy_signal)
    full_noisy_fit = function_Sine(xs,popt[0],popt[1],popt[2])
    clean_mod = Mod_Depth(clean_signal)
    noisy_mod = Mod_Depth(full_noisy_fit)

    ax.clear()
    ax.plot(x_deg,clean_signal,label='Clean Signal',color='r')
    ax.scatter(x_deg,white_noise,s=9,label='White Noise')
    ax.scatter(x_deg,shot_noise,s=9,label='Shot Noise')
    ax.plot(x_deg,full_noisy_signal,label='Full Noisy Signal',color='green')
    ax.plot(x_deg,full_noisy_fit,label='Full Noisy Fit',color='cyan')
    ax.hlines(y=0,xmin=0,xmax=np.max(x_deg),color='k')
    ax.vlines(x=0,ymin=0,ymax=np.max(full_noisy_signal),color='k')
    ax.set_title(f'Noise Effect on Modulation Depth\nClean M = {clean_mod:.2f}, Noisy M = {noisy_mod:.2f}')
    
    ax.legend()

    fig.canvas.draw_idle()

fig, ax = plt.subplots(figsize=(8,6))


ax_slider_white_noise = fig.add_axes([0.2, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_white_noise = Slider(ax_slider_white_noise, 'White Noise Scale', 0, 5, valinit=white_noise_scale)

ax_slider_shot_noise = fig.add_axes([0.2, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_shot_noise = Slider(ax_slider_shot_noise, 'Shot Noise Scale', 0, 1, valinit=shot_noise_scale)

slider_white_noise.on_changed(update)
slider_shot_noise.on_changed(update)

update(None)


plt.show()