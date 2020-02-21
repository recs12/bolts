""" Replace all fasteners from imperial to metric.
"""

from api import Api, PartsOccurrences, PartElement
from sources import screwlib_path

def main():
    session = Api()
    print("* Author: recs")
    print("* Last update: 2020-00-00")
    session.check_valid_version('Solid Edge ST7','Solid Edge 2019')
    assembly = session.active_document()
    print("* part-number: %s\n" % assembly.name)

    # Check if part is sheetmetal or other type of part.
    assert assembly.name.endswith(".asm"), "This macro only works on .asm not %s" %assembly.name[-4:]

    parts = PartsOccurrences(assembly)

    # Display quantity of parts in the assembly.
    quantites(parts.count_fasteners, parts.count_imperial, parts.count_metric)

    # Replace screws.
    for part in parts.screws():
        screw =  PartElement(part)
        print(screw.name)
        replaced_part = screw.replace_metric()
        print(replaced_part)


    #TODO: Reprint quantity after the process done.
    quantites(parts.count_fasteners, parts.count_imperial, parts.count_metric, state="(Changed state)")


def quantites(total, count_imperial, count_metric, state="(Current state)"):
    #TODO: number of screws, nuts, washers
    print("{}".format(state))
    print("Total number of fasteners: {}\n".format(total))
    print("...............- imperial: {}\n".format(count_imperial))
    print("...............- metric  : {}\n".format(count_metric))

def confirmation(func):
    response = raw_input(
    """Bolts converts screws,nuts,washers from imperial to metric, (Press y/[Y] to proceed.): """
    )
    if response.lower() not in ['y']:
        print('Process canceled')
        sys.exit()
    else:
        func()


if __name__ == "__main__":
    confirmation(main)