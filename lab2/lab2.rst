:Author: Justin Perona
:Copyright: © 2020 Justin Perona
:License: CC BY-NC 4.0

========================
ECS 154A - Lab 2 WQ 2020
========================

.. contents::
  :local:

Logistics
---------

Submission
~~~~~~~~~~

Due by 20:00 on Monday, 2020-02-03.

Turn in for the Logisim portion is on Gradescope.
Submit the specified .circ files for each problem.
The person submitting should specify their partner's name (if necessary) during the submission process.

Turn in for the survey is on Canvas.
Each person needs to submit a survey, even if they worked with a partner.
More information on the survey is at the end of this document.

Logisim Evolution, Grading, and Debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Need a reminder on how to download Logisim Evolution, how your circuits are autograded, or how to debug your circuits?
Check the relevant sections of the `Lab 1 document`_.

.. _`Lab 1 document`: https://github.com/jlperona-teaching/ecs154a-winter20/blob/master/lab1/lab1.rst

Constraints
~~~~~~~~~~~

For these problems, you must use designs relying on only the following, unless specified otherwise:

* basic gates (NOT, AND, OR, NAND, NOR, XOR, XNOR)
* MUXes
* decoders
* the Logisim wiring library

Violating specified constraints will result in a 0 on the problem in question.
While the autograder may give you credit even if you violate a constraint, we will check submissions after the due date and update grades appropriately.

Logisim Problems [95]
---------------------

1. MUX function implementation [5]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *1.circ*
* Main circuit name: *muxfunction*
* Input pin(s): *fourbitinput* [4]
* Output pin(s): *f* [1]

Implement the following function using a MUX:

    f(A, B, C, D) = m0 + m1 + m3 + m5 + m9 + m11 + m12

You may not use gates for this problem.
You may only use MUXes, splitters, constants, power, and ground.

2. Decoder function implementation [5]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *2.circ*
* Main circuit name: *decoderfunction*
* Input pin(s): *fourbitinput* [4]
* Output pin(s): *g* [1]

Implement the following function using a one-hot decoder:

    f(A, B, C, D) = m1 + m2 + m5 + m8 + m13 + m14 + m15

The only type of basic gate you may use for this problem is the OR gate.
Apart from OR gates, you may only use decoders, splitters, constants, power, and ground.

3. Bit counting [5]
~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *3.circ*
* Main circuit name: *bitcounting*
* Input pin(s): *twelvebitinput* [12]
* Output pin(s): *zeroes* [4]

Suppose we want to determine how many of the bits in a twelve-bit unsigned number are equal to zero.
Implement the simplest circuit that can accomplish this task.

You may use any Logisim component for this problem.

4. Comparator implementation [5]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *4.circ*
* Main circuit name: *comparison*
* Input pin(s): *inputa* [8], *inputb* [8]
* Output pin(s): *areequal* [1]

Implement an 8-bit comparator.

While already specified above, you may not use anything from the Arithmetic library for this problem.
This defeats the purpose of the problem.
You must implement your comparator within the constraints specified for this lab.

5. Parity checker [5]
~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *5.circ*
* Main circuit name: *parity*
* Input pin(s): *tenbitinput* [10]
* Output pin(s): *evenparity* [11]

Implement a simple even parity checker.
Given a ten-bit number, output an 11th bit that ensures the total number of bits that are 1 is even.
Concatenate this bit to the original number as the least significant bit.

There are parity gates for both type of parity.
It defeats the purpose of this problem if you use those, so you may not use either of them.
That said, it's possible to finish this problem using only a single gate.

6. 4-bit carry-lookahead unit [15]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *6.circ*
* Main circuit name: *cla*
* Input pin(s): *inputa* [4], *inputb* [4], *carryin* [1]
* Output pin(s): *carryout* [4], *generator* [4], *propagator* [4]

Implement a 4-bit carry-lookahead unit (CLA).
For the given *carryin* and each bit of the given inputs *inputa* and *inputb*, generate the relevant *carryout* bits.
You will also need to output the corresponding *generator* and *propagator* bits.

Your CLA must be a true CLA.
If your unit ripples the carry rather than calculating each carry based on the *generator* and *propagator* bits, you will get a 0.
The calculations for each bit of *carryout* should only be using *carryin* and not any *carryout* values you calculate.

While already specified above, you may not use anything from the Arithmetic library for this problem.
Normally, you would use gate outputs inside a full adder for your generate and propagate signals.
Instead, you will need to create those gates inside this circuit.

7. 4-bit ALU [25]
~~~~~~~~~~~~~~~~~

* Submission file for this part: *7.circ*
* Main circuit name: *alu*
* Input pin(s): *inputa* [4], *inputb* [4], *operation* [3]
* Output pin(s): *aluout* [4]

I highly recommend that you finish the previous problem before starting this one.

Design a 4-bit ALU.
Given the following input as the *operation* line, each bit cell of the ALU should perform the appropriate operation:

* 000 = AND
* 001 = NOT B
* 010 = OR
* 011 = SUB (A - B)
* 100 = XOR
* 101 = NOT A
* 110 = ADD (A + B)
* 111 = (reserved for future use)

All arithmetic operations will be on 2's complement numbers.
This only matters for the ADD and SUB operations, since the others are performed bitwise.
Overflows are expected; you do not need to do anything special in those cases.

Your ADD and SUB operations must use a carry-lookahead unit rather than being a ripple-carry adder.
Use the one you created in the previous problem.
If you create a ripple-carry adder instead of using your previous circuit, you will lose points.

I highly recommend creating a subcircuit for a single bit cell of the ALU that operates on a single bit of each input.
I also recommend using probes for this part for the inputs, the various operations, the selector line, and the output of the ALU.
This will make your debugging much easier.

While already specified above, you may not use anything from the Arithmetic library for this problem.
You will get a 0 if you use the built-in adder or subtractor; create the logic for those operations using gates.
You will also lose points if you are using a ripple-carry adder; see above for more details.

8. Error correcting [30]
~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *8.circ*
* Main circuit name: *errorcorrecting*
* Input pin(s): *inputdata* [15]
* Output pin(s): *correcteddata* [11]

Implement an 11-bit variant of the Hamming(7,4) error correction method that we discussed in class.
We will have 11 data bits, and 4 check bits to cover said data bits.
You will need to determine the position of the data and check bits, as well as which check bits cover which data bits.
The lecture notes on error correction will be helpful in laying out the circuit.
Hint: you will want to use a decoder to correctly route to the bit you want to invert, if any.

To save time and make debugging easier, I *highly recommend* giving descriptive tunnel names to each of the individual bits of *inputdata* once you have determined which bit is which.
This will make the process of calculating the check bits much easier to visualize.

Upon receiving the input, you will need to recalculate the check bits, and use those to determine which bit has been flipped, if any.
Errors will only be of size 1, if there are any at all.
You do not need to worry about errors of size 2 or greater.

Survey [5]
----------

You can find the `survey for this lab`_ on Canvas.
Reminder: each person needs to submit a survey individually, even if they worked with a partner.

.. _`survey for this lab`: https://canvas.ucdavis.edu/courses/424855/quizzes/54945
