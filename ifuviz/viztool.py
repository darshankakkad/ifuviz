import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits

def initiate_viztool(sci_cube, wl):  
    # Collapsed image for reference
    sci_cube[np.isnan(sci_cube)] = 0
    collapsed_image = np.sum(sci_cube, axis=0)
    
    # --- Interactive plot ---
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(8, 9.2), gridspec_kw={"height_ratios": [2, 1]})
    img = ax0.imshow(collapsed_image, origin='lower', cmap='viridis',vmin=0, vmax=0.008*np.max(collapsed_image))
    spec_line, = ax1.plot([], [], label='Data')
    #model_line, = ax1.plot([], [], label='Model')
    
    def onclick(event):
        if event.inaxes == ax0:
            i, j = int(event.xdata), int(event.ydata)
            spectrum = sci_cube[:, j, i]
            #model = cont_cube[:, j, i]
            spec_line.set_data(wl, spectrum)
            #model_line.set_data(wl, model)
            ax1.set_xlim(wl[0], wl[-1])
            ax1.set_ylim(np.min(spectrum)*0.9, np.max(spectrum)*1.1)
            fig.canvas.draw_idle()

    ax0.tick_params(labelsize=14)
    ax0.set_title("Click on a pixel to view spectrum", fontsize=16)

    ax1.tick_params(labelsize=14)
    ax1.set_xlabel("Wavelength [A]",fontsize=16)
    ax1.set_ylabel("Flux", fontsize=16)
    ax1.legend()
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    
    plt.tight_layout()
    plt.show()
