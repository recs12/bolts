""" Replace all fasteners from imperial to metric.
"""

import sys

from api import Api, PartElement, PartsOccurrences


def replace_parts():
    try:
        material = prompt_selection()
        session = Api()
        print("\n* Author: recs")
        print("* Last update: 2020-04-17")
        session.check_valid_version("Solid Edge ST7", "Solid Edge 2019")
        assembly = session.active_document()
        print("* part-number: {}\n".format(assembly.name))

        # Check if part is sheetmetal or other type of part.
        assert assembly.name.endswith(
            ".asm"
        ), "This macro only works on .asm not {}".format(assembly.name[-4:])

        parts = PartsOccurrences(assembly)

        # Display quantity of parts in the assembly.
        quantites(parts.count_fasteners, parts.count_imperial, parts.count_metric)

        print(" " + 60 * "-")
        print("{:^30s}->{:^30s}".format("Current", "Changed to"))
        print(" " + 60 * "=")

        # Replace screws.
        for part in parts.screws():
            screw = PartElement(part)
            screw_name_initial = screw.name
            screw_name_changed = screw.set_material(material)
            screw.replace_element(screw_name_changed)
            print(" {:<30s} {:<30s}".format(screw_name_initial, screw_name_changed))

        # # Replace nuts.
        for part in parts.nuts():
            nut = PartElement(part)
            nut_name_initial = nut.name
            nut_name_changed = nut.set_material(material)
            nut.replace_element(nut_name_changed)
            print(" {:<30s} {:<30s}".format(nut_name_initial, nut_name_changed))

        # # Replace washers.
        for part in parts.washers():
            washer = PartElement(part)
            washer_name_initial = washer.name
            washer_name_changed = washer.set_material(material)
            washer.replace_element(washer_name_changed)
            print(" {:<30s} {:<30s}".format(washer_name_initial, washer_name_changed))

        print(" " + 60 * "-")
        print("\n")

        quantites(
            parts.count_fasteners,
            parts.count_imperial,
            parts.count_metric,  # add others counts
            state="(Changed state)",
        )

    except NameError as Ne:
        # TODO: add the name of the fastener in a log file in the user tempo.
        pass
    else:
        pass
    finally:
        raw_input("\n(Press any key to exit ;)")
        sys.exit()


def quantites(total, count_imperial, count_metric, state="(Current state)"):
    """
    Display quantites of fasteners.

    Description:
        Maint to show the user before and after the excution of the macro.

    Parameters: ...

    """
    print("{}".format(state))
    print("Total number of fasteners: {}".format(total))
    print(" - imperial: ............. {}".format(count_imperial))
    print(" - metric  : ............. {}".format(count_metric))
    print(" - [2] Metric  [Zinc Plated]")
    print(" - [3] Imperial [SS-304]")
    print(" - [4] Metric   [SS-304]")
    print(" - [5] Imperial [SS-316]")
    print(" - [6] Metric   [SS-316]")


def confirmation(func):
    """ Prompt the user to confirm the execution of the process."""
    response = raw_input(
        """\nBolts: Converts fasteners from imperial to metric, (Press y/[Y] to proceed.): """
    )
    if response.lower() not in ["y"]:
        print("Process canceled")
        sys.exit()
    else:
        func()


def prompt_selection():
    choice = raw_input(
        """
        select:
            [1] - Cancel
            [2] - Metric  [Zinc Plated]
            [3] - Imperial [SS-304]
            [4] - Metric   [SS-304]
            [5] - Imperial [SS-316]
            [6] - Metric   [SS-316]
        """
    )

    return {
        1: "Cancel",
        2: "Metric [Zinc Plated]",
        3: "Imperial [SS-304]",
        4: "Metric [SS-304]",
        5: "Imperial [SS-316]",
        6: "Metric [SS-316]",
    }.get(choice)


if __name__ == "__main__":
    confirmation(replace_parts)
