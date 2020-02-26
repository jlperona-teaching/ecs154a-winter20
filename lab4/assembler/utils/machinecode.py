from math import ceil

# representation of a single line of machine code
# defined via each line of the input csv file

# bit width definitions
op_bits = 4
rd_bits = 3
rs1_bits = 3
rs2_bits = 3
imm_bits = 8
all_bits = op_bits + rd_bits + rs1_bits + rs2_bits + imm_bits

# 0-based instead of 1-based
min_register_number = 0
max_register_number = pow(2, rd_bits) - 1

# -2^(imm bits) to 2^(imm bits) - 1
min_immediate = -pow(2, imm_bits)
max_immediate = pow(2, imm_bits) - 1

# dictionary for opcode lookup
opcode_dict = {
    'NOP':   0,
    'NOT':   1,
    'AND':   2,
    'XOR':   3,
    'OR':    4,
    'ADD':   5,
    'SUB':   6,
    'MOV':   7,
    'MOVI':  8,
    'ADDI':  9,
    'SUBI': 10,
    'SLL':  11,
    'SRL':  12,
    'CMP':  13,
    'HLT':  14,
    'HCF':  15
}

# https://stackoverflow.com/a/12946226
def bindigits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

class MachineCode:

    def __init__(self, op, rd, rs1, rs2, imm, row):
        # input variables taken from CSV file
        self.op = str(op)
        self.rd = str(rd)
        self.rs1 = str(rs1)
        self.rs2 = str(rs2)
        self.imm = str(imm)

        # binary variables after checking originals for correctness
        self.op_bin = None
        self.rd_bin = None
        self.rs1_bin = None
        self.rs2_bin = None
        self.imm_bin = None

        # final concatenation variables
        self.bin = None
        self.hex = None

        # debugging
        self.row = str(row)

    def convert_op(self):
        try:
            self.op = self.op.upper()

            if self.op in opcode_dict:
                op_temp = opcode_dict[self.op]

                self.op_bin = bindigits(op_temp, op_bits)
            else:
                raise ValueError
        except ValueError: # invalid input
            invalid_op_exception = str('Invalid op input \'' + self.op
                + '\' on row \'' + self.row + '\'.')
            raise Exception(invalid_op_exception) from None

    def convert_rd(self):
        try:
            rd_temp = int(self.rd)

            if rd_temp > max_register_number or rd_temp < min_register_number:
                raise ValueError

            self.rd_bin = bindigits(rd_temp, rd_bits)
        except ValueError: # invalid input
            invalid_rd_exception = str('Invalid rd input \'' + self.rd
                + '\' on row \'' + self.row + '\'.')
            raise Exception(invalid_rd_exception) from None

    def convert_rs1(self):
        try:
            rs1_temp = int(self.rs1)

            if rs1_temp > max_register_number or rs1_temp < min_register_number:
                raise ValueError

            self.rs1_bin = bindigits(rs1_temp, rs1_bits)
        except ValueError: # invalid input
            invalid_rs1_exception = str('Invalid rs1 input \'' + self.rs1
                + '\' on row \'' + self.row + '\'.')
            raise Exception(invalid_rs1_exception) from None

    def convert_rs2(self):
        try:
            rs2_temp = int(self.rs2)

            if rs2_temp > max_register_number or rs2_temp < min_register_number:
                raise ValueError

            self.rs2_bin = bindigits(rs2_temp, rs2_bits)
        except ValueError: # invalid input
            invalid_rs2_exception = str('Invalid rs2 input \'' + self.rs2
                + '\' on row \'' + self.row + '\'.')
            raise Exception(invalid_rs2_exception) from None

    def convert_imm(self):
        try:
            imm_temp = int(self.imm)

            if imm_temp > max_immediate or imm_temp < min_immediate:
                raise ValueError

            self.imm_bin = bindigits(imm_temp, imm_bits)
        except ValueError: # invalid input
            invalid_imm_exception = str('Invalid imm input \'' + self.imm
                + '\' on row \'' + self.row + '\'.')
            raise Exception(invalid_imm_exception) from None

    def convert_to_bin(self):
        self.convert_op()
        self.convert_rd()
        self.convert_rs1()
        self.convert_rs2()
        self.convert_imm()

        self.bin = (self.op_bin + self.rd_bin
            + self.rs1_bin + self.rs2_bin + self.imm_bin)

    def convert_to_hex(self):
        # first 0: positional argument for format to specify what to convert
        # colon: modify the formatting of that positional argument
        # second 0: don't place the typical 0x for hex
        # width: named argument for number of bits to format to
        # x: lower case hexadecimal formatting
        # int(self.bin, 2): convert binary concatentation back into integer format
        # ceil(all_bits / 4): calculate hex width from binary and take the ceiling of the result
        self.hex = '{0:0{width}x}'.format(int(self.bin, 2), width = ceil(all_bits / 4))

    def output_bin(self):
        return str(self.bin + '\n')

    def output_hex(self):
        return str(self.hex + '\n')
