from ifuviz.viztool import initiate_viztool
from ifuviz.loaddata import load_cube

def main():
    sci_cube, wl = load_cube()
    initiate_viztool(sci_cube, wl)
