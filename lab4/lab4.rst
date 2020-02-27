:Author: Justin Perona
:Copyright: © 2020 Justin Perona
:License: CC BY-NC 4.0

========================
ECS 154A - Lab 4 WQ 2020
========================

.. contents::
  :local:

Logistics
---------

Submission
~~~~~~~~~~

Due by 20:00 on Friday, 2020-03-13.

Turn in for the Logisim Evolution portion is on Gradescope.
Submit the specified .circ files for each problem.
The person submitting should specify their partner's name (if necessary) during the submission process.

Turn in for the survey is on Canvas.
Each person needs to submit a survey, even if they worked with a partner.
More information on the survey is at the end of this document.

Logisim Evolution and Grading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Need a reminder on how to download Logisim Evolution or how your circuits are autograded?
Check the relevant sections of the `Lab 1 document`_.

.. _`Lab 1 document`: https://github.com/jlperona-teaching/ecs154a-winter20/blob/master/lab1/lab1.rst#logisim-evolution

Debugging and Testing Sequential Circuits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Need a reminder on how to debug and test sequential circuits?
Check the relevant sections of the `Lab 3 document`_.

.. _`Lab 3 document`: https://github.com/jlperona-teaching/ecs154a-winter20/blob/master/lab3/lab3.rst#debugging-sequential-circuits

Logisim Evolution Problems [95]
-------------------------------

Background
~~~~~~~~~~

Your final task (at least, in terms of the labs) will be to build a single cycle CPU.
This is considered a rite of passage for computer architecture courses.
This CPU will be 8 bits wide, and can do various register transfers and ALU operations using point-to-point connections.

In typical fashion for this course, the first couple of problems in this lab have you implement pieces of the CPU in isolation and test them for correct operation.
We start small and build our way up.
This is also set up this way so that you can get some partial credit if you can't complete the entire thing.
However, a good portion of credit for the lab will come from the final problem where you combine your pieces and create a working CPU.
It's much more important to understand how these pieces fit together and build off of each other, hence the point setup.

Below is an outline of the overall CPU design.

CPU Diagram
"""""""""""

You should follow the diagram below when building your CPU.
Some of the control wires are not on the diagram.
You will need to figure out how to implement those yourself.

.. image:: cpu-diagram.png
    :align: center
    :width: 100%

In the following problems, you will implement the following portions.
See the individual problems for more information on each portion.

#. ALU
#. PC and RAM
#. Register File
#. A Select Unit, B Select Unit, Control Unit, and connecting everything together

CPU Design Philosophy
"""""""""""""""""""""

The design for this machine is different from any that have been produced in industry.
However, it does draw heavily from some previous designs.
Some of the naming conventions for signals in the diagram above have been borrowed from the open-source `RISC-V instruction set architecture`_.
The meaning of some of the names is below:

* *wen*: write enable
* *op*: operation code or opcode
* *rd*: register destination
* *rs1*: register source 1
* *rs2*: register source 2
* *imm*: immediate value
* *x0-x7*: register designation for register 0 through register 7

However, this is not a RISC-V machine.
In case you are interested in learning more about RISC-V, or building your own CPUs in something other than Logisim Evolution, I'd highly recommend taking ECS 154B.
You build multiple RISC-V CPUs in that class using a `hardware design language (HDL)`_ called Chisel_.

.. _`RISC-V instruction set architecture`: https://en.wikipedia.org/wiki/RISC-V
.. _`hardware design language (HDL)`: https://en.wikipedia.org/wiki/Hardware_description_language
.. _Chisel: https://www.chisel-lang.org/

Instruction Format
""""""""""""""""""

The following table describes how a 21-bit instruction for this CPU will be formatted:

+----------+----------+-------------------------------+--------------------------------------------------------------------------------+
| **Name** | **Bits** | **Function in CPU**           | **Description**                                                                |
+----------+----------+-------------------------------+--------------------------------------------------------------------------------+
| *op*     | 20 - 17  | ALU Control                   | Determines which operation to perform and immediate mode operand sourcing.     |
+----------+----------+-------------------------------+--------------------------------------------------------------------------------+
| *rd*     | 16 - 14  | Register File Register Select | Destination register specification.                                            |
+----------+----------+-------------------------------+--------------------------------------------------------------------------------+
| *rs1*    | 13 - 11  | A Select Unit Control         | Primary source register specification.                                         |
+----------+----------+-------------------------------+--------------------------------------------------------------------------------+
| *rs2*    | 10 - 8   | B Select Unit Control         | Secondary source register specification. Not always used on every instruction. |
+----------+----------+-------------------------------+--------------------------------------------------------------------------------+
| *imm*    | 7 - 0    | Immediate Value Input Data    | Unsigned input data. Not always used on every instruction.                     |
+----------+----------+-------------------------------+--------------------------------------------------------------------------------+

Operation Description
"""""""""""""""""""""

The following table describes what the opcode from the table above corresponds to in terms of operation.
All operations, except for NOP, HLT, and HCF, place their results in the destination register *rd*.

+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Operation** | **op [20-17]** | **Description**                                                                                                                                                      |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NOP           | 0000           | No OPeration. No registers, other than the PC, should change during this instruction cycle.                                                                          |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NOT           | 0001           | Negate *rs1*; place the result in *rd*.                                                                                                                              |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AND           | 0010           | Bitwise AND of *rs1* and *rs2*; place the result in *rd*.                                                                                                            |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| XOR           | 0011           | Bitwise XOR of *rs1* and *rs2*; place the result in *rd*.                                                                                                            |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OR            | 0100           | Bitwise OR of *rs1* and *rs2*; place the result in *rd*.                                                                                                             |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADD           | 0101           | Add *rs1* and *rs2*; place the result in *rd*. You must use a carry-lookahead unit.                                                                                  |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SUB           | 0110           | Subtract *rs2* from *rs1*; place the result in *rd*. You must use a carry-lookahead unit.                                                                            |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MOV           | 0111           | Copy *rs1* as is; place the result in *rd*.                                                                                                                          |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MOVI          | 1000           | Copy *imm* as is; place the result in *rd*.                                                                                                                          |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADDI          | 1001           | Add *rs1* and *imm*; place the result in *rd*. You must use a carry-lookahead unit.                                                                                  |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SUBI          | 1010           | Subtract *imm* from *rs1*; place the result in *rd*. You must use a carry-lookahead unit.                                                                            |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SLL           | 1011           | Shift all bits of *rs1* to the left by 1, discard the left-most bit, and make the least significant bit 0; place the result in *rd*.                                 |
|               |                +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|               |                | SLL stands for Shift Left Logical. Example: 1011 -> 0110.                                                                                                            |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SRL           | 1100           | Shift all bits of *rs1* to the right by 1, discard the right-most bit, and make the most significant bit 0; place the result in *rd*.                                |
|               |                +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|               |                | SRL stands for Shift Right Logical. Example: 1011 -> 0101.                                                                                                           |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CMP           | 1101           | Compare. If *rs1* == *rs2*, output a 1, otherwise output 0; place the result in *rd*.                                                                                |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HLT           | 1110           | Halt. Stop the CPU from executing any further instructions until a reset. The PC will continue to increment.                                                         |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HCF           | 1111           | Stop the CPU from executing any further instructions until a fire extinguisher (reset) is used. The PC will no longer increment until the fire extinguisher is used. |
|               |                +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|               |                | HCF stands for `Halt and Catch Fire`_. The CPU literally halts and catches fire.                                                                                     |
+---------------+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _`Halt and Catch Fire`: https://en.wikipedia.org/wiki/Halt_and_Catch_Fire

Constraints
"""""""""""

For these problems, you must use designs relying on only the following, unless specified otherwise:

* the Logisim Evolution Wiring library
* the Logisim Evolution Gates library
* the Logisim Evolution Plexers library
* flip flops from the Logisim Evolution Memory library
* RAM, registers, and counters from the Logisim Evolution Memory library
* shifters from the from the Logisim Evolution Arithmetic library
* comparators from the from the Logisim Evolution Arithmetic library

ROMs are explicitly disallowed.
Adders and subtractors are also explicitly disallowed.
Make them via gates like you have in the past.

1. 8-bit ALU [25]
~~~~~~~~~~~~~~~~~

* Submission file for this part: *1.circ*
* Main circuit name: *alu8*
* Input pin(s): *a* [8], *b* [8], *op* [4]
* Output pin(s): *rddata* [8]

Create an 8-bit ALU.
This portion of the CPU handles the calculations based on stored and current input values.

You have already designed a 4-bit ALU in Lab 2.
The general format of this ALU will look very similar to that one, and you should be able to use your previous work as a starting point.
However, this ALU will operate on more bits and implement more possible operations.
Make sure to perform operations bitwise in this lab's ALU.

Operations
""""""""""

Based on the *opcode*, the ALU will perform a certain operation.
The result of the operation is output as *rddata*.
For details on which operation is which *op* value, check the `Operation Description`_ section above.

Note that NOP, HLT, and HCF don't actually use the ALU.
Those opcodes won't be provided in this problem.
When combining everything together, you will need to figure out how to handle those three instructions.

Carry Look-ahead for Adding and Subtracting
"""""""""""""""""""""""""""""""""""""""""""

For the adder and subtractor, you must use carry look-ahead for each group of 4 bits.
Note that you have already built a 4-bit CLA unit in Lab 2, assuming we didn't mark you for rippling the carry.

Below is a clarification on what carry look-ahead means.
There was a lot of confusion on this in the last lab, which is why I changed it to not deduct any points if you did build a ripple-carry adder.
A carry look-ahead unit calculates all carries at the same time using all the propagator and generator bits, without reusing any carry bits.
A carry bit you calculate should not feed into any other logic, nor should you duplicate the logic for a carry bit to use in another piece of logic.

The above means that:

* Your equation for C1 should purely be in terms of C0.
* Your equation for C2 should purely be in terms of C0. C1 should not appear in your logic at all.
* Your equation for C3 should purely be in terms of C0. C1 and C2 should not appear in your logic at all.
* Your equation for C4 should purely be in terms of C0. C1, C2, and C3 should not appear in your logic at all.

Since you are using carry look-ahead for each group of 4 bits, C4 should be used as the base for C5, C6, and C7.
This means that:

* Your equation for C5 should purely be in terms of C4.
* Your equation for C6 should purely be in terms of C4. C5 should not appear in your logic at all.
* Your equation for C7 should purely be in terms of C4. C5 and C6 should not appear in your logic at all.

You should have a maximum of 8 OR gates across both CLAs.
You should be able to figure out how to reuse your previous CLA unit here, if it was correct.
You may disregard the final carry out.

This time, you *will* be deducted points if you build a ripple-carry adder.
If anything above is confusing, look at the lecture notes on adders, or ask on Campuswire.

2. PC and RAM [15]
~~~~~~~~~~~~~~~~~~

* Submission file for this part: *2.circ*
* Main circuit name: *instructions*
* Input pin(s): *resetall* [1], *sysclock* [1]
* Output pin(s): *pc* [8], *op* [4], *rd* [3], *rs1* [3], *rs2* [3], *imm* [8]

Create the program counter (PC) and the random access memory (RAM) that stores the instructions and outputs the current instruction.
This portion of the CPU gives the commands to the remainder of the CPU to calculate and store values.

Program Counter
"""""""""""""""

The PC will be an 8-bit up-counter that starts at 0 and wraps around upon saturation.
You may use the built-in counter module to do so.
I have to allow registers for the next part, and you can make a counter pretty easily out of a register and an adder or ALU.

The output of the PC, *pc*, will feed the RAM the memory location of the instruction it should output.
In addition, you will need to attach the *resetall* signal to the reset pins of the flip flops in your PC.
When *resetall* is asserted, the PC should be reset to 0.
This is used to reset the CPU back to the start.

Random Access Memory
""""""""""""""""""""

The output of the PC, *pc*, will be fed to a 256 entry x 21 data RAM module with separate load and store ports.
We will only use the RAM as a source of instructions, so we will not use the store port.
The address bits will be sourced from the output of your PC.
The output of the RAM will be the relevant pieces of the instruction that you should be executing on this cycle.

Make sure to change the databus implementation over to separate databuses for reading and writing.
You will need to hook up *sysclock* to the C3 pin of the RAM.
In addition, make sure to hook up a ground module to the M1 pin of the RAM, and a power module to the M2 pin of the RAM.
Doing these will ensure that the RAM outputs the instruction value and does not attempt to overwrite any data.

Loading Programs
""""""""""""""""

If you are manually testing this subcircuit, you will want to set the initial contents of your RAM to the tester file *ram/cpu.txt*.
If you click on the RAM, on the left sidebar there is an option for *Initial contents* that you'll want to use.

When you are testing this via the tester, you'll need to make a slight change to the command line argument you use.
You should add ``-load ram/4.txt`` to the end of the command.
This tells Logisim Evolution to load the RAM in your subcircuit with the expected program.
Thus, a full command for the tester for this part will look like this:

.. code-block:: bash

    java -jar logisim-evolution.jar tester/2tester.circ -tty table -load ram/cpu.txt > output.txt
    diff output.txt tsv/2.tsv

There should only be one RAM in this circuit or any subcircuits used in this file.
Make sure the address and data sizes are correct.
We will attempt to load the RAM with the tester program via the ``-load`` command line argument.
This command will attempt to load *every* RAM with the file we specify.
Having more than one will lead to undesired results.
Using a ROM will prevent us from loading programs and you will get a 0.

3. Register File [15]
~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *3.circ*
* Main circuit name: *regfile*
* Input pin(s): *rd* [3], *rddata* [8], *wen* [1], *resetall* [1], *sysclock* [1]
* Output pin(s): *x0* [8], *x1* [8], *x2* [8], *x3* [8], *x4* [8], *x5* [8], *x6* [8], *x7* [8]

Create an eight-bit eight-register register file.
This portion of the CPU provides the storage for the rest of the CPU.

Although a CPU would normally store output in memory (RAM), we will not be dealing with memory in this lab.
Instead, we will treat the values of the registers as the "output" of this CPU, hence all the output pins.

Write Enable and Reset
""""""""""""""""""""""

On the rising edge of *sysclock*, if the *wen* signal is asserted, the register corresponding to the appropriate *rd* value will be written with *rddata*.
The registers' current values will be output as *x0* through *x7*.
Hint: much like the Hamming(7,4) circuit, a decoder will be very useful here.

Note that in this problem, *wen* will be provided for you.
You should hook this up to the appropriate pin on the register module.
When combining everything together, you will need to determine when *wen* should be 0 or 1.

Additionally, you will need to attach the *resetall* signal to the reset pin of your registers.
When this signal is asserted, all registers should be reset to 0.
This is used to reset the CPU back to the start.

Subcircuits and Constraints
"""""""""""""""""""""""""""

You should (and effectively must) use registers to implement this problem.
Flip flops don't have a write enable pin, which causes an interesting side effect when playing with the clock on attempting to disable a write.

You may not use RAM to implement your register file; doing so will result in a 0 for this problem.
Using a RAM will cause your CPU to break when we use the ``-load`` command line argument for the next problem.

4. Single Cycle CPU [40]
~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *4.circ*
* Main circuit name: *cpu*
* Input pin(s): *resetall* [1], *sysclock* [1]
* Output pin(s): *pc* [8], *x0* [8], *x1* [8], *x2* [8], *x3* [8], *x4* [8], *x5* [8], *x6* [8], *x7* [8]

Finally, put all the pieces together from the previous parts and build your single cycle CPU according to the diagram.
A good portion of credit for the lab is on this problem.

This part doesn't take many extra components to implement, not including the subcircuits for the previous parts.
You shouldn't be adding a ton of extra logic here, but you will need to spend some time and think about what you're implementing.
When importing the subcircuits from the previous parts, you can use the *Merge...* option under *File* in the menu bar.
This way, you don't need to copy and paste.

Your only input pins here are *sysclock* and *resetall*.
*sysclock* is used to make sure the tester circuit and your CPU stay in lockstep.
*resetall* won't be used for this part but may be helpful for your manual testing.
Make sure to hook these inputs up to both the PC, the register file, and any flip flops you add in this circuit specifically.

The output pins are *pc* and *x0* through *x7*.
*pc* is used to make sure your PC is incrementing correctly (or not, depending on the situation).
*x0* through *x7* is to check your CPU for correctness.

Here's some more detail on the other parts of the CPU you haven't implemented yet:

A Select
""""""""

This multiplexer selects between the different registers for the A input into the ALU.
*rs1* specifies which register becomes A.

B Select
""""""""

This unit selects between the different registers or the immediate data input *imm* for the B input into the ALU.
*rs2* will specify which register becomes B, but this doesn't apply for every instruction.
When we say "immediate value," we mean the last 8 bits contained with the instruction itself.
For the MOVI, ADDI, and SUBI instructions, the B data source to the ALU should be the 8 bits from the instruction, instead of the value from the register specified by *rs2*.
This is why *imm* feeds into the B select logic.

You will need to figure out this block of logic by yourself.
It will look similar to the `A Select`_ unit above, but not exactly the same.

Program Counter Special Cases
"""""""""""""""""""""""""""""

There are two special cases you need to deal with for the PC that you did not need to deal with before.
Control wires from your control unit will be a good way to handle these cases.
It is up to you to figure out how to implement the functionality for both.

It is possible to implement both of these special cases without modifying your subcircuits for any of the pieces you've made already.
Feel free to modify your subcircuits for those parts if you think you need to.
That said, make sure to only modify the subcircuits inside this problem instead of your previous ones.
If you make changes to the previous ones, then they may fail the autograder.

* If a HLT instruction was decoded, then the PC still needs to advance.

  * Any future instructions after the HLT (except for HCF) should not modify the CPU until the *resetall* signal is given.
  * If HCF is detected afterwards then that takes precedence.

    * Even if you've halted, you can't exactly ignore being set on fire.
    * Perform the same functionality below if you detect an HCF after a HLT.

  * It is possible that *resetall* is not given at all and the PC will roll over.

* If a HCF instruction was decoded, then the PC needs to stop completely.

  * Your CPU is on fire now. Hopefully you have insurance.
  * The PC should stay at the value when *hcf* was asserted.

    * Your CPU doesn't need to recover from an HCF via a *resetall* trigger.
    * In my own testing, the RAM won't advance even after *resetall* is triggered.
    * If you need to reset your CPU during manual testing, you can use ``Ctrl-R`` to do so.

  * Hint: there's at least two ways of doing this.

    * One way will be very similar to the logic for implementing HLT above. However, if you do it this way, you will need to modify the PC and RAM subcircuit.
    * Another mechanism would be to modify *sysclock* specifically for the PC subcircuit.

Control Unit
""""""""""""

The control unit contains the logic to set the ALU to perform the correct operation.
You can pass *op* along as is to the ALU.

The control unit also generates control wires for the rest of the CPU to use.
The exact wires are up to you.
Here are some recommendations:

* You'll want to figure out how to generate *wen* here.

  * In the register file problem, the value was given to you.
  * You will need to figure out when it should be 0 or 1 and generate it yourself now.

* You'll want to design logic so that the B Select unit selects the correct value for certain instructions.

  * If you have an immediate-type instruction, you should select the *imm* data.
  * See the `B Select`_ section for more information on this.

* You'll probably want to design logic for HLT and HCF here as well.

  * It'll be helpful to do so here rather than inside the PC and RAM subcircuit.
  * See the `Program Counter Special Cases`_ section for more information on HLT and HCF.

Loading Programs
""""""""""""""""

If you are manually testing this subcircuit, you will want to set the initial contents of your RAM to the tester file *ram/cpu.txt*.
If you click on the RAM, on the left sidebar there is an option for *Initial contents* that you'll want to use.

When you are testing this via the tester, you'll need to make a slight change to the command line argument you use.
You should add ``-load ram/4.txt`` to the end of the command.
This tells Logisim Evolution to load the RAM in your subcircuit with the expected program.
Thus, a full command for the tester for this part will look like this:

.. code-block:: bash

    java -jar logisim-evolution.jar tester/4tester.circ -tty table -load ram/cpu.txt > output.txt
    diff output.txt tsv/4.tsv

There should only be one RAM in this circuit or any subcircuits used in this file.
Make sure the address and data sizes are correct.
We will attempt to load the RAM with the tester program via the ``-load`` command line argument.
This command will attempt to load *every* RAM with the file we specify.
Having more than one will lead to undesired results.
Using a ROM will prevent us from loading programs and you will get a 0.

Assembler
"""""""""

There is a Python 3 script inside the *assembler/* subdirectory.
You can use this to build your own programs for further testing or your own experimentation.

Use the ``-h`` flag to understand how the assembler expects its command line arguments.
The input CSV file should look similar to *ram/cpu.csv*.

Other Considerations
""""""""""""""""""""

If you add any other flip flops to your circuit here, make sure to hook them up to *sysclock* so they stay in sync with the grader circuit.
Also, make sure to hook up the *resetall* pin to them as well so that they reset correctly.

Survey [5]
----------

You can find the `survey for this lab`_ on Canvas.
Reminder: each person needs to submit a survey individually, even if they worked with a partner.

Please be truthful on the survey and submit it *after* you finish the lab.
I do these surveys to check how people feel about the lab and to see if I need to make changes in the future.

.. _`survey for this lab`: https://canvas.ucdavis.edu/courses/424855/quizzes/54947

Extra credit: Transaction ledger [15]
-------------------------------------

* Submission file for this part: *extracredit.circ*
* Main circuit name: *ledger*
* Input pin(s): *customerid* [3], *transactiontype* [2], *transactionamount* [8], *sysclock* [1]
* Output pin(s): *transactionresult* [2], *amountremaining* [8]

Background
~~~~~~~~~~

Hsakaa, Treepnura, Tihcra, and Nitsuj (names changed to protect the innocent) are regulars at the Sankiro Brewery in Davis.
One night, during a drunken haze, they had a brilliant idea, or so they thought.
Why should Sankiro keep paying a percentage fee (somewhere around 2.5%) and flat fee (somewhere around $0.15) per transaction to credit card companies like Asiv or Dracretsam (names changed to avoid potential legal liability) to handle credit card transactions?
If they just built a transaction ledger, and everybody was honest about it, then Sankiro could make their beers cheaper, and thus the group could order more beer for the same amount of money!

Now, there's a couple of problems with this idea:

#. They came up with this idea after reaching, then obliterating, the Ballmer peak
#. They thought people would be honest on the ledger
#. They thought Sankiro would make their beers cheaper if they didn't have to pay transaction fees anymore
#. The group thought they would actually be able to handle the increased amount of beer they thought they'd be getting

You'll notice that the thing that's not on the list above is "it's impossible to create the transaction ledger."
Nitsuj is lazy and is outsourcing it to his SCE A451 students as extra credit.
However, Nitsuj believes that extra credit should truly be "extra."
While he's providing a framework here, it's up to the students to figure out some parts.

Details
~~~~~~~

There will only be 8 customers you need to handle; each one has a unique *customerid*.
You may assume that each customer's balance is 0 at the start.
The maximum amount is $255; we don't bother with cents here.
Each clock cycle, a new transaction request will come in with a *customerid*, *transactiontype*, and *transactionamount*.
You will need to handle the transaction and output the appropriate *transactionresult* and *amountremaining* in that customer's balance.

The input *transactiontype* indicates the following:

* **00**: Query balance, disregard input transaction amount
* **01**: Attempt to add money to account
* **10**: Attempt to debit money from account
* **11**: (reserved for future use)

The output *transactionresult* indicates the following:

* **00**: Transaction was a query, output current balance
* **01**: Transaction accepted, output new balance
* **10**: Add transaction rejected due to trying to put in too much money, output current balance
* **11**: Debit transaction rejected due to not having enough money (AKA life), output current balance

You can treat all balances and transaction amounts as unsigned numbers.
Hint: one of the output pins of the arithmetic modules you will use provides a simple way of handling overflows and underflows.

Testing and Grading
~~~~~~~~~~~~~~~~~~~

The tester file for this part contains two programs.
The first one is a randomized stress tester using a pseudo-random number generator.
This is what your extra credit problem will be tested upon for correctness.

The second one, inside the ROM, corresponds to the contents in *ram/extracredit.txt*.
*ram/extracredit.csv* explains how this file is formatted.
It is a much simpler program designed to test certain cases for *transactiontype* and *transactionresult*.
This one will not be used during the grading process; it is solely to help you test your circuit.

If you would like to change between the two for your testing purposes, change the constant for *programchoice* inside the tester file to 0 or 1.

Constraints
~~~~~~~~~~~

You may use anything from the following for this problem:

* the Logisim Evolution Wiring library
* the Logisim Evolution Gates library
* the Logisim Evolution Plexers library
* the Logisim Evolution Arithmetic library
* registers from the Logisim Evolution Memory library

You may not use ROMs or RAM; doing so will result in a 0.
Make your storage out of register modules.
