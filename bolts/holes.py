#!python3
# Units: 0 (inch) & 1 (mm)
from customs import savedholes
from equivalences import mapping


class Hole:
    def __init__(self, hole):
        self.hole = hole


    # Allow to check the parameters of hole
    # also, it can be used as extractor of datahole
    def __repr__(self):
        return """{
            "BottomAngle": "%s",
            "CounterboreDepth": "%s",
            "CounterboreDiameter": "%s",
            "CounterboreProfileLocationType": "%s",
            "CountersinkAngle": "%s",
            "CountersinkDiameter": "%s",
            "Fit": "%s",
            "HeadClearance": "%s",
            "HoleDiameter": "%s",
            "HoleType": "%s",
            "InsideEffectiveThreadLength": "%s",
            "OutsideEffectiveThreadLength": "%s",
            "Size": "%s",
            "Standard": "%s",
            "SubType": "%s",
            "Taper": "%s",
            "TaperDimType": "%s",
            "TaperLValue": "%s",
            "TaperMethod": "%s",
            "TaperRValue": "%s",
            "ThreadDepth": "%s",
            "ThreadDepthMethod": "%s",
            "ThreadDescription": "%s",
            "ThreadDiameterOption": "%s",
            "ThreadExternalDiameter": "%s",
            "ThreadHeight": "%s",
            "ThreadMinorDiameter": "%s",
            "ThreadNominalDiameter": "%s",
            "ThreadSetting": "%s",
            "ThreadTapDrillDiameter": "%s",
            "ThreadTaperAngle": "%s",
            "TreatmentType": "%s",
            "Units": "%s",
            "VBottomDimType": "%s",
        },""" % (
            self.hole.BottomAngle,
            self.hole.CounterboreDepth,
            self.hole.CounterboreDiameter,
            self.hole.CounterboreProfileLocationType,
            self.hole.CountersinkAngle,
            self.hole.CountersinkDiameter,
            self.hole.Fit,
            self.hole.HeadClearance,
            self.hole.HoleDiameter,
            self.hole.HoleType,
            self.hole.InsideEffectiveThreadLength,
            self.hole.OutsideEffectiveThreadLength,
            self.hole.Size,
            self.hole.Standard,
            self.hole.SubType,
            self.hole.Taper,
            self.hole.TaperDimType,
            self.hole.TaperLValue,
            self.hole.TaperMethod,
            self.hole.TaperRValue,
            self.hole.ThreadDepth,
            self.hole.ThreadDepthMethod,
            self.hole.ThreadDescription,
            self.hole.ThreadDiameterOption,
            self.hole.ThreadExternalDiameter,
            self.hole.ThreadHeight,
            self.hole.ThreadMinorDiameter,
            self.hole.ThreadNominalDiameter,
            self.hole.ThreadSetting,
            self.hole.ThreadTapDrillDiameter,
            self.hole.ThreadTaperAngle,
            self.hole.TreatmentType,
            self.hole.Units,
            self.hole.VBottomDimType,
        )

    def inspection_hole(self):
        print("%s - HOLEDATA" % self.hole.Size)
        print(" ")
        print("   BottomAngle: %s" % self.hole.BottomAngle)
        print("   CounterboreDepth: %s" % self.hole.CounterboreDepth)
        print("   CounterboreDiameter: %s" % self.hole.CounterboreDiameter)
        print(
            "   CounterboreProfileLocationType: %s"
            % self.hole.CounterboreProfileLocationType
        )
        print("   CountersinkAngle: %s" % self.hole.CountersinkAngle)
        print("   CountersinkDiameter: %s" % self.hole.CountersinkDiameter)
        print("   Fit: %s" % self.hole.Fit)
        print("   HeadClearance: %s" % self.hole.HeadClearance)
        print("   HoleDiameter: %s" % self.hole.HoleDiameter)
        print("   HoleType: %s" % self.hole.HoleType)
        print(
            "   InsideEffectiveThreadLength: %s" % self.hole.InsideEffectiveThreadLength
        )
        print(
            "   OutsideEffectiveThreadLength: %s"
            % self.hole.OutsideEffectiveThreadLength
        )
        print("   Size: %s" % self.hole.Size)
        print("   Standard: %s" % self.hole.Standard)
        print("   SubType: %s" % self.hole.SubType)
        print("   Taper: %s" % self.hole.Taper)
        print("   TaperDimType: %s" % self.hole.TaperDimType)
        print("   TaperLValue: %s" % self.hole.TaperLValue)
        print("   TaperMethod: %s" % self.hole.TaperMethod)
        print("   TaperRValue: %s" % self.hole.TaperRValue)
        print("   ThreadDepth: %s" % self.hole.ThreadDepth)
        print("   ThreadDepthMethod: %s" % self.hole.ThreadDepthMethod)
        print("   ThreadDescription: %s" % self.hole.ThreadDescription)
        print("   ThreadDiameterOption: %s" % self.hole.ThreadDiameterOption)
        print("   ThreadExternalDiameter: %s" % self.hole.ThreadExternalDiameter)
        print("   ThreadHeight: %s" % self.hole.ThreadHeight)
        print("   ThreadMinorDiameter: %s" % self.hole.ThreadMinorDiameter)
        print("   ThreadNominalDiameter: %s" % self.hole.ThreadNominalDiameter)
        print("   ThreadSetting: %s" % self.hole.ThreadSetting)
        print("   ThreadTapDrillDiameter: %s" % self.hole.ThreadTapDrillDiameter)
        print("   ThreadTaperAngle: %s" % self.hole.ThreadTaperAngle)
        print("   TreatmentType: %s" % self.hole.TreatmentType)
        print("   Units: %s" % self.hole.Units)
        print("   VBottomDimType: %s" % self.hole.VBottomDimType)
        print("\n")
    
    @property
    def size(self):
        return self.hole.Size

    def get_equivalence(self):
        if not self.hole.SubType:
            raise Exception("[-] SubType value undefined")
        else:
            if self.hole.Standard == "ANSI Metric - PT":
                print("[-] %s already metric. \n\n" % self.hole.Name)
            else:
                size = self.hole.Size  # check for size
                if not isinstance(size, str):
                    raise ValueError("size is not string.")
                else:
                    pass

                equiv = mapping.get(size, None)
                if equiv not in savedholes:
                    raise ValueError(
                        "Hole size: %s is not in costums-holes-collection." % size
                    )
                if not isinstance(equiv, str):
                    raise TypeError("equiv is not string.")
                else:
                    pass

                hole_data = savedholes.get(equiv)
                if not isinstance(hole_data, dict):
                    raise TypeError("hole_data is not dict type: %s" % type(hole_data))
                else:
                    return hole_data

    def conversion_to_metric(self, db):
        if not db:
            pass
        else:
            self.hole.Units = db.get("Units", None)
            self.hole.BottomAngle = db.get("BottomAngle", None)
            self.hole.CounterboreDepth = db.get("CounterboreDepth", None)
            self.hole.CounterboreDiameter = db.get("CounterboreDiameter", None)
            self.hole.CounterboreProfileLocationType = db.get(
                "CounterboreProfileLocationType", None
            )
            self.hole.CountersinkAngle = db.get("CountersinkAngle", None)
            self.hole.CountersinkDiameter = db.get("CountersinkDiameter", None)
            self.hole.HeadClearance = db.get("HeadClearance", None)
            self.hole.HoleDiameter = db.get("HoleDiameter", None)
            self.hole.HoleType = db.get("HoleType", None)
            self.hole.Size = db.get("Size", None)
            self.hole.Standard = db.get("Standard", None)
            self.hole.SubType = db.get("SubType", None)
            self.hole.Taper = db.get("Taper", None)
            self.hole.TaperDimType = db.get("TaperDimType", None)
            self.hole.TaperLValue = db.get("TaperLValue", None)
            self.hole.TaperMethod = db.get("TaperMethod", None)
            self.hole.TaperRValue = db.get("TaperRValue", None)
            self.hole.ThreadDepth = db.get("ThreadDepth", None)
            self.hole.ThreadDepthMethod = db.get("ThreadDepthMethod", None)
            self.hole.ThreadDescription = db.get("ThreadDescription", None)
            self.hole.ThreadDiameterOption = db.get("ThreadDiameterOption", None)
            self.hole.ThreadExternalDiameter = db.get("ThreadExternalDiameter", None)
            # self.hole.ThreadHeight= db.get("ThreadHeight", None)
            # ValueError: Value does not fall within the expected range.
            self.hole.ThreadMinorDiameter = db.get("ThreadMinorDiameter", None)
            self.hole.ThreadNominalDiameter = db.get("ThreadNominalDiameter", None)
            self.hole.ThreadSetting = db.get("ThreadSetting", None)
            self.hole.ThreadTapDrillDiameter = db.get("ThreadTapDrillDiameter", None)
            self.hole.ThreadTaperAngle = db.get("ThreadTaperAngle", None)
            self.hole.TreatmentType = db.get("TreatmentType", None)
            self.hole.VBottomDimType = db.get("VBottomDimType", None)


# TODO: [3] create method quick_inspection (just /size)
