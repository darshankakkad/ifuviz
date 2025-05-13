# ifuviz/viztool.py

import numpy as np
import matplotlib.pyplot as plt

def initiate_viztool(cube, model_cube, wl_array):
    Nz, Ny, Nx = np.shape(cube)
    cube[np.isnan(cube)] = 0
    collapse_img = np.sum(cube, axis=0)

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={"height_ratios": [1, 2]})
    img = ax0.imshow(collapse_img, origin='lower', cmap='hot',\
                     extent=[-Nx/2,Nx/2,-Ny/2,Ny/2])

    spec_line, = ax1.plot([], [], label='Data', color='grey')
    model_line, = ax1.plot([], [], label='Model', color='red')

    def onclick(event):
        if event.inaxes == ax0:
            i, j = int(event.xdata), int(event.ydata)
            spectrum = cube[:, j, i]
            model_spec = model_cube[:, j, i]
            spec_line.set_data(wl_array, spectrum)
            model_line.set_data(wl_array, model_spec)
            ax1.set_margins(x=0)
            fig.canvas.draw_idle()

    ax1.set_title("TBC: From header")
    ax1.set_xlabel("Wavelength [arb unit]")
    ax1.set_ylabel("Flux [arb unit]")
    ax1.legend()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.tight_layout()
    plt.show()
