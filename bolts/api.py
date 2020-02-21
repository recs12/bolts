
"""
Api solidedge
=======================

"""

import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import sys, os
import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import SolidEdgeConstants as SEConstants
import System.Runtime.InteropServices as SRI

from screws import INVENTORY_SCREWS
from nuts import INVENTORY_NUTS
from washers import INVENTORY_WASHERS
from cad_convertor import CONVERTION_CAD
from sources import screwlib_path



class Api():

    def __init__(self):
        # Connect to a running instance of Solid Edge
        self.api = SRI.Marshal.GetActiveObject("SolidEdge.Application")

    @property
    def name(self):
        return self.Name

    def check_valid_version(self, *valid_version):
        #validate solidedge version - 'Solid Edge ST7'
        print("* version: %s" %self.api.Value)
        assert self.api.Value in valid_version, "Unvalid version of solidedge"

    def active_document(self):
        return self.api.ActiveDocument



class PartsOccurrences():

    def __init__(self, doc):
        self.occurrences = doc.Occurrences
        self.count = self.occurrences.Count

    @property
    def name(self):
        return self.Name

    def screws(self):
        return (screw for screw in self.occurrences if screw.PartDocument.name in INVENTORY_SCREWS)

    def nuts(self):
        return (nut for nut in self.occurrences if nut.PartDocument.name in INVENTORY_NUTS)

    def washers(self):
        return (washer for washer in self.occurrences if washer.PartDocument.name in INVENTORY_WASHERS)

    @property
    def count_fasteners(self):
        fasteners = [fast for fast in self.occurrences if fast.PartDocument.Name in CONVERTION_CAD.keys()+CONVERTION_CAD.values()]
        return len(fasteners)

    @property
    def count_imperial(self):
        fasteners = [fast for fast in self.occurrences if fast.PartDocument.Name in CONVERTION_CAD.keys()]
        return len(fasteners)

    @property
    def count_metric(self):
        fasteners = [fast for fast in self.occurrences if fast.PartDocument.Name in CONVERTION_CAD.values()]
        return len(fasteners)

class PartElement():

    def __init__(self, doc):
        self.name = doc.PartDocument.Name
        self.part = doc

    def replace_metric(self):
        metric_equivalent = CONVERTION_CAD.get(self.part.PartDocument.Name)
        metric_screw = os.path.join(screwlib_path, metric_equivalent)
        self.part.Replace(
            NewOccurrenceFileName = metric_screw,
            ReplaceAll = True,
        )
        return metric_equivalent