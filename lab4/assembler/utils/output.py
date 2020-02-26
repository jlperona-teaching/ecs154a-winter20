import sys

from utils.machinecode import MachineCode

# write results to output file
def write_output(args, all_machine_code):
    logisim_evolution_rom_header = 'v2.0 raw\n'

    # write output to file if defined
    if args.outfile:
        with open(args.outfile, 'w') as outfile:
            outfile.write(logisim_evolution_rom_header)

            for current_machine_code in all_machine_code:
                if args.binary:
                    outfile.write(current_machine_code.output_bin())
                else:
                    outfile.write(current_machine_code.output_hex())
    # else write output to stdout
    else:
        sys.stdout.write(logisim_evolution_rom_header)

        for current_machine_code in all_machine_code:
            if args.binary:
                sys.stdout.write(current_machine_code.output_bin())
            else:
                sys.stdout.write(current_machine_code.output_hex())
