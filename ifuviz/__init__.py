from ifuviz.viztool import initiate_viztool
from ifuviz.loaddata import load_cube

def main():
    sci_cube, wl = load_cube("/Users/dk24abv/work/research_projects/BASS/MUSE/LZIFU/data/NGC7469.fits")
    initiate_viztool(sci_cube, wl)
