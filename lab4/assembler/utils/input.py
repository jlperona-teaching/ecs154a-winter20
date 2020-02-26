import csv
import sys

from utils.machinecode import MachineCode

# input file parsing
def parse_input(args, all_machine_code):
    # open file and begin reading data
    with open(args.infile) as infile:
        csvreader = csv.reader(infile)

        # skip header line depending on command line arguments
        if args.noheader == False:
            next(csvreader)

        # for every line in the csv file
        for row in csvreader:
            line_number = csvreader.line_num

            row_it = iter(row)
            column_number = -1

            # process five columns with data, skip any remaining columns
            try:
                column_number += 1
                op = next(row_it)

                column_number += 1
                rd = next(row_it)

                column_number += 1
                rs1 = next(row_it)

                column_number += 1
                rs2 = next(row_it)

                column_number += 1
                imm = next(row_it)
            except StopIteration:
                invalid_assembly_exception = str(
                    'Not enough data input on row ' + str(line_number) + '.'
                )
                raise Exception(invalid_assembly_exception) from None

            # create new machine code
            current_machine_code = MachineCode(op, rd, rs1, rs2, imm, line_number)
            all_machine_code.append(current_machine_code)
