# ifuviz/viztool.py

import numpy as np
import matplotlib.pyplot as plt

def initiate_viztool(cube, model_cube, wl_array):
    Nz, Ny, Nx = np.shape(cube)
    cube[np.isnan(cube)] = 0
    collapse_img = np.sum(cube, axis=0)

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(8, 9.2), gridspec_kw={"height_ratios": [2, 1]})
    img = ax0.imshow(collapse_img, origin='lower', cmap='hot')

    spec_line, = ax1.plot([], [], label='Data', color='grey')
    #model_line, = ax1.plot([], [], label='Model', color='red')

    def onclick(event):
        if event.inaxes == ax0:
            i, j = int(event.xdata), int(event.ydata)
            spectrum = cube[:, j, i]
            #model_spec = model_cube[:, j, i]
            spec_line.set_data(wl_array, spectrum)
            model_line.set_data(wl_array, model_spec)
            ax1.set_margins(x=0)
            fig.canvas.draw_idle()

    ax1.set_title("Click on a pixel to view the spectrum")
    ax1.set_xlabel("Wavelength")
    ax1.set_ylabel("Flux")
    ax1.legend()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.tight_layout()
    plt.show()
