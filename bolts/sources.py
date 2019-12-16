
# Path to the cache of the user
#TODO: customize the path with the current user using os
usercache = r"C:\Users\recs\AppData\Roaming\Unigraphics Solutions\Solid Edge\SEEC\http_plm.premiertech.com_tc_\recs\Default"

# Path to cad models libraries for Nuts, Screw, Washer.
nutslib_path = r"J:\PTCR\_Tools\Librairie\Hardware\Nuts"
screwlib_path = r"J:\PTCR\_Tools\Librairie\Hardware\Screw"
washerlib_path = r"J:\PTCR\_Tools\Librairie\Hardware\Washer"

# Mapping fasteners imperial - metric
jde_mapping = {
    '24100034':'185560',
}

# model_mapping is generated from jde_mapping.
model_mapping = {
    "VTHE_0.500-13X3.000_GR5.par": "VTHE_M12-1.75X075_SS.par",
}

# Warning: .par of .PAR has consequences on search.
collection_screws = {
    "VTHE_0.500-13X3.000_GR5.par": "24100034",
    "VTHE_M12-1.75X075_SS.par": "185560",
}

collection_nuts = {
    "E_AB_M12-1.50": "24101757",
}

