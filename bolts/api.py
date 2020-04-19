"""
Api solidedge
=======================

"""

import json
import os

import clr

import System.Runtime.InteropServices as SRI

# from convertion import CONVERTION_CAD
# from inventory import INVENTORY_NUTS, INVENTORY_SCREWS, INVENTORY_WASHERS
with open("inventory.json") as i:
    inventory = json.load(i)

# from cad_switcher import cad_switcher
with open("tree.json") as t:
    tree = json.load(t)

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")


# Path to cad library for Nuts, Screw, Washer.
# CAD = r"..\hardware"
CAD = r"J:\PTCR\Users\RECS\hardware"


class Api:
    def __init__(self):
        # Connect to a running instance of Solid Edge
        self.api = SRI.Marshal.GetActiveObject("SolidEdge.Application")

    @property
    def name(self):
        return self.Name

    def check_valid_version(self, *valid_version):
        # validate solidedge version - 'Solid Edge ST7'
        print("* version: {}".format(self.api.Value))
        assert self.api.Value in valid_version, "Unvalid version of solidedge"

    def active_document(self):
        return self.api.ActiveDocument


class PartsOccurrences:
    def __init__(self, doc):
        self.occurrences = doc.Occurrences
        self.count = self.occurrences.Count

    @property
    def name(self):
        return self.Name

    def screws(self):
        return (
            screw
            for screw in self.occurrences
            if screw.PartDocument.name in inventory.get("SCREWS")
        )

    def nuts(self):
        return (
            nut
            for nut in self.occurrences
            if nut.PartDocument.name in inventory.get("NUTS")
        )

    def washers(self):
        return (
            washer
            for washer in self.occurrences
            if washer.PartDocument.name in inventory.get("WASHER")
        )

    @property
    def count_fasteners(self):
        fasteners = [
            fast
            for fast in self.occurrences
            if fast.PartDocument.Name in CONVERTION_CAD.keys() + CONVERTION_CAD.values()
        ]
        return len(fasteners)

    @property
    def count_imperial(self):
        fasteners = [
            fast
            for fast in self.occurrences
            if fast.PartDocument.Name in CONVERTION_CAD.keys()
        ]
        return len(fasteners)

    @property
    def count_metric(self):
        fasteners = [
            fast
            for fast in self.occurrences
            if fast.PartDocument.Name in CONVERTION_CAD.values()
        ]
        return len(fasteners)


class PartElement:
    def __init__(self, item):
        self.part = item
        self.name = item.PartDocument.Name

    def set_material(self, material):
        if self.name in fasteners.keys():
            return fasteners.get(self.name, {}).get(material)
        else:
            return "unknown"

    def replace_element(self, new_element):
        if new_element == "unknown":
            # log the name of a log file for correction on the convertion file.
            pass
        elif new_element is None:
            pass
        else:
            self.part.Replace(
                NewOccurrenceFileName=os.path.join(CAD, new_element), ReplaceAll=True
            )
