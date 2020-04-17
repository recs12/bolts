""" Replace all fasteners from imperial to metric.
"""

import sys

from api import Api, PartElement, PartsOccurrences


def main():
    try:
        session = Api()
        print("\n* Author: recs")
        print("* Last update: 2020-02-25")
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
            screw_name_imperial = screw.name
            screw_name_metric = screw.set_metric()
            screw.replace_element(screw_name_metric)
            print(" {:<30s} {:<30s}".format(screw_name_imperial, screw_name_metric))

        # # Replace nuts.
        for part in parts.nuts():
            nut = PartElement(part)
            nut_name_imperial = nut.name
            nut_name_metric = nut.set_metric()
            nut.replace_element(nut_name_metric)
            print(" {:<30s} {:<30s}".format(nut_name_imperial, nut_name_metric))

        # # Replace washers.
        for part in parts.washers():
            washer = PartElement(part)
            washer_name_imperial = washer.name
            washer_name_metric = washer.set_metric()
            washer.replace_element(washer_name_metric)
            print(" {:<30s} {:<30s}".format(washer_name_imperial, washer_name_metric))

        print(" " + 60 * "-")
        print("\n")

        quantites(
            parts.count_fasteners,
            parts.count_imperial,
            parts.count_metric,
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
    print(" - metric  : ............. {}\n".format(count_metric))


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


if __name__ == "__main__":
    confirmation(main)
