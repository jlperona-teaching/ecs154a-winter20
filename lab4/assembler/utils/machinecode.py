from math import ceil


# bit width definitions
op_bits = 4
rd_bits = 3
rs1_bits = 3
rs2_bits = 3
imm_bits = 8
all_bits = op_bits + rd_bits + rs1_bits + rs2_bits + imm_bits

# registers are 0-based instead of 1-based
min_register_number = 0
max_register_number = pow(2, rd_bits) - 1

# immediate range: -2^(imm bits) to 2^(imm bits) - 1
min_immediate = -pow(2, imm_bits)
max_immediate = pow(2, imm_bits) - 1

# dictionary for opcode lookup
opcode_dict = {
    'NOP': 0,
    'NOT': 1,
    'AND': 2,
    'XOR': 3,
    'OR': 4,
    'ADD': 5,
    'SUB': 6,
    'MOV': 7,
    'MOVI': 8,
    'ADDI': 9,
    'SUBI': 10,
    'SLL': 11,
    'SRL': 12,
    'CMP': 13,
    'HLT': 14,
    'HCF': 15
}


def bindigits(n, bits):
    """From an integer n, return a string with the binary representation.
    The binary representation extends out to bits length.
    The first bit represents the sign of the number.
    Credit given to https://stackoverflow.com/a/12946226.
    """
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


class MachineCode:
    """Representation of a single line of machine code.
    Each code is defined via each line of the input CSV file.
    """
    def __init__(self, op: str, rd: str, rs1: str,
                 rs2: str, imm: str, row: int) -> None:
        """Inits MachineCode with the individual portions of the CSV line."""
        # input variables taken from CSV file
        self._op = op
        self._rd = rd
        self._rs1 = rs1
        self._rs2 = rs2
        self._imm = imm

        # binary variables after checking originals for correctness
        self._op_bin = ""
        self._rd_bin = ""
        self._rs1_bin = ""
        self._rs2_bin = ""
        self._imm_bin = ""

        # final concatenation variables
        self._bin = ""
        self._hex = ""

        # debugging
        self._row = str(row)

    def convert_op(self) -> None:
        """Take in a string containing the opcode for this code.
        Convert the given opcode string to its binary representation.
        """
        try:
            self._op = self._op.upper()

            if self._op in opcode_dict:
                op_temp = opcode_dict[self._op]

                self._op_bin = bindigits(op_temp, op_bits)
            else:
                raise ValueError
        except ValueError:  # invalid input
            invalid_op_exception = str(
                'Invalid op input \'' + self._op + '\' on row \''
                + self._row + '\'.'
            )
            raise Exception(invalid_op_exception) from None

    def convert_rd(self) -> None:
        """Take in a string containing the destination register for this code.
        Convert the given destination register to its binary representation.
        """
        try:
            rd_temp = int(self._rd)

            if rd_temp > max_register_number or rd_temp < min_register_number:
                raise ValueError

            self._rd_bin = bindigits(rd_temp, rd_bits)
        except ValueError:  # invalid input
            invalid_rd_exception = str(
                'Invalid rd input \'' + self._rd + '\' on row \''
                + self._row + '\'.'
            )
            raise Exception(invalid_rd_exception) from None

    def convert_rs1(self) -> None:
        """Take in a string containing the 1st source register for this code.
        Convert the given source register to its binary representation.
        """
        try:
            rs1_temp = int(self._rs1)

            if (rs1_temp > max_register_number
                    or rs1_temp < min_register_number):
                raise ValueError

            self._rs1_bin = bindigits(rs1_temp, rs1_bits)
        except ValueError:  # invalid input
            invalid_rs1_exception = str(
                'Invalid rs1 input \'' + self._rs1 + '\' on row \''
                + self._row + '\'.'
            )
            raise Exception(invalid_rs1_exception) from None

    def convert_rs2(self) -> None:
        """Take in a string containing the 2nd source register for this code.
        Convert the given source register to its binary representation.
        """
        try:
            rs2_temp = int(self._rs2)

            if (rs2_temp > max_register_number
                    or rs2_temp < min_register_number):
                raise ValueError

            self._rs2_bin = bindigits(rs2_temp, rs2_bits)
        except ValueError:  # invalid input
            invalid_rs2_exception = str(
                'Invalid rs2 input \'' + self._rs2 + '\' on row \''
                + self._row + '\'.'
            )
            raise Exception(invalid_rs2_exception) from None

    def convert_imm(self) -> None:
        """Take in a string containing the immediate value for this code.
        Covert the immediate value to its binary representation.
        """
        try:
            imm_temp = int(self._imm)

            if imm_temp > max_immediate or imm_temp < min_immediate:
                raise ValueError

            self._imm_bin = bindigits(imm_temp, imm_bits)
        except ValueError:  # invalid input
            invalid_imm_exception = str(
                'Invalid imm input \'' + self._imm + '\' on row \''
                + self._row + '\'.'
            )
            raise Exception(invalid_imm_exception) from None

    def convert_to_bin(self) -> None:
        """Run the conversion functions for all portions of this code.
        Concatenate them to set this code's binary representation.
        """
        self.convert_op()
        self.convert_rd()
        self.convert_rs1()
        self.convert_rs2()
        self.convert_imm()

        self._bin = (self._op_bin + self._rd_bin + self._rs1_bin
                     + self._rs2_bin + self._imm_bin)

    def convert_to_hex(self) -> None:
        """Take the binary representation of this code and convert to hex.
        Below explains each part of this one-liner.

        first 0: positional argument for format to specify what to convert
        colon: modify the formatting of that positional argument
        second 0: don't place the typical 0x for hex
        width: named argument for number of bits to format to
        x: lower case hexadecimal formatting
        int(self._bin, 2): convert binary concat. back into integer format
        ceil(all_bits / 4): calculate hex width from binary
                            then take the ceiling of the result
        """
        self._hex = '{0:0{width}x}'.format(int(self._bin, 2),
                                           width=ceil(all_bits / 4))

    def output_bin(self) -> str:
        """Return the binary representation of this code as a string."""
        return str(self._bin + '\n')

    def output_hex(self) -> str:
        """Return the hex representation of this code as a string."""
        return str(self._hex + '\n')
