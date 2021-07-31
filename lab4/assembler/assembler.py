import utils.commandline
import utils.input
import utils.output

from utils.machinecode import MachineCode
from typing import List


def main() -> None:
    """Take in input CSV with assembler instructions.
    Write assembly hex to stdout or output file.
    """
    # command line argument processing
    args = utils.commandline.argument_parsing()

    # input file processing
    all_machine_code: List['MachineCode'] = []
    utils.input.parse_input(args, all_machine_code)

    # data processing
    for current_machine_code in all_machine_code:
        current_machine_code.convert_to_bin()
        current_machine_code.convert_to_hex()

    # output file processing
    utils.output.write_output(args, all_machine_code)


if __name__ == "__main__":
    main()
