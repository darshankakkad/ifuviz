# A standalone code that is useful in visualising a cube and the input models. 
# Files have been hard-coded here, but will be modified in future versions

import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits

# Load raw data
cube_file = fits.open("/Users/dk24abv/work/research_projects/BASS/MUSE/LZIFU/data/NGC7469.fits")
hdr = cube_file[0].header
sci_cube = cube_file[0].data
Nz, Ny, Nx = np.shape(sci_cube)
wl = (np.linspace(1,Nz,Nz) - hdr["CRPIX3"])*hdr["CDELT3"] + hdr["CRVAL3"]

# Load the model. You may need to change extensions etc
model_file = fits.open("/Users/dk24abv/work/research_projects/BASS/MUSE/LZIFU/products/NGC7469_1_comp.fits")
cont_cube = model_file[1].data

# Collapsed image for reference
sci_cube[np.isnan(sci_cube)] = 0
collapsed_image = np.sum(sci_cube, axis=0)

# --- Interactive plot ---
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(8, 9.2), gridspec_kw={"height_ratios": [2, 1]})
img = ax0.imshow(collapsed_image, origin='lower', cmap='viridis',vmin=0, vmax=0.008*np.max(collapsed_image))
ax0.set_title("Click on a pixel to view spectrum")
spec_line, = ax1.plot([], [], label='Data')
model_line, = ax1.plot([], [], label='Model')
ax1.set_xlabel("Wavelength [A]")
ax1.set_ylabel("Flux")
ax1.legend()

def onclick(event):
    if event.inaxes == ax0:
        i, j = int(event.xdata), int(event.ydata)
        spectrum = sci_cube[:, j, i]
        model = cont_cube[:, j, i]
        spec_line.set_data(wl, spectrum)
        model_line.set_data(wl, model)
        ax1.set_xlim(wl[0], wl[-1])
        ax1.set_ylim(np.min(spectrum)*0.9, np.max(spectrum)*1.1)
        fig.canvas.draw_idle()

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.tight_layout()
plt.show()
