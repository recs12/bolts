
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

from sources import collection_screws, model_mapping, screwlib_path

class Api():

    def __init__(self):
        # Connect to a running instance of Solid Edge
        self.api = SRI.Marshal.GetActiveObject("SolidEdge.Application")

    @property
    def name(self):
        return self.Name

    def check_valid_version(self, *valid_version):
        #validate solidedge version - 'Solid Edge ST7'
        print("version solidedge: %s" %self.api.Value)
        assert self.api.Value in valid_version, "Unvalid version of solidedge"

    def active_document(self):
        return self.api.ActiveDocument

class HoleCollection():

    def __init__(self, doc):
        self.holes = doc.HoleDataCollection
        self.count = self.holes.Count

    def threaded(self):
        return (hole for hole in self.holes if hole.SubType=="Standard Thread")

class PartsOccurrences():

    def __init__(self, doc):
        self.occurrences = doc.Occurrences
        self.count = self.occurrences.Count

    @property
    def name(self):
        return self.Name

    def screws(self):
        return (screw for screw in self.occurrences if screw.PartDocument.name in collection_screws)


class PartElement():

    def __init__(self, doc):
        self.name = doc.PartDocument.Name
        self.part = doc
    
    def replace_metric(self):
        metric_equivalent = model_mapping.get(self.part.PartDocument.Name)
        metric_screw = os.path.join(screwlib_path, metric_equivalent)
        self.part.Replace(
            NewOccurrenceFileName = metric_screw,
            ReplaceAll = True,
        )