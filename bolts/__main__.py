""" Convert threads in holes from imperial to metric.
"""

import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import sys, os
import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import SolidEdgeConstants as SEConstants
import System.Runtime.InteropServices as SRI

from api import Api, PartsOccurrences, PartElement
from sources import collection_screws, model_mapping, screwlib_path

def main():
    session = Api()
    print("Author: recs")
    print("Last update: 2020-00-00")
    session.check_valid_version('Solid Edge ST7','Solid Edge 2019')
    assembly = session.active_document()
    print("part: %s\n" % assembly.name)

    # Check if part is sheetmetal or other type of part.
    assert assembly.name.endswith(".asm"), "This macro only works on .asm not %s" %assembly.name[-4:]

    parts = PartsOccurrences(assembly)
    print("Total number of items: %s\n" %parts.count)

    # Replace screws.
    for part in parts.screws():
        screw =  PartElement(part)
        print(screw.name)
        screw.replace_metric()

if __name__ == "__main__":
    main()