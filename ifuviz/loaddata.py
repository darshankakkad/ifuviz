import astropy.io.fits as fits
import numpy as np

def load_cube(input_file):
    # Load data
    cube_file = fits.open(input_file)
    hdr = cube_file[0].header
    sci_cube = cube_file[0].data
    Nz, Ny, Nx = np.shape(sci_cube)
    wl = (np.linspace(1,Nz,Nz) - hdr["CRPIX3"])*hdr["CDELT3"] + hdr["CRVAL3"]

    #model_file = fits.open("/Users/dk24abv/work/research_projects/BASS/MUSE/LZIFU/products/NGC7469_1_comp.fits")
    #cont_cube = model_file[1].data
    return sci_cube, wl
