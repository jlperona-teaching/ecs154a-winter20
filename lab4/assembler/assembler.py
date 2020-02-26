import utils.commandline
import utils.input
import utils.output

from utils.machinecode import MachineCode

# command line argument processing
args = utils.commandline.argument_parsing()

# input file processing
all_machine_code = []
utils.input.parse_input(args, all_machine_code)

# data processing
for current_machine_code in all_machine_code:
    current_machine_code.convert_to_bin()
    current_machine_code.convert_to_hex()

# output file processing
utils.output.write_output(args, all_machine_code)
