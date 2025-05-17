import astropy.io.fits as fits
import numpy as np

def load_cube():
    cube_file = fits.open("/Users/dk24abv/work/research_projects/BASS/MUSE/LZIFU/data/NGC7469.fits")
    hdr = cube_file[0].header
    sci_cube = cube_file[0].data
    Nz, Ny, Nx = np.shape(sci_cube)
    wl = (np.linspace(1,Nz,Nz) - hdr["CRPIX3"])*hdr["CDELT3"] + hdr["CRVAL3"]
    return sci_cube, wl
