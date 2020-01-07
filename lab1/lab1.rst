:Author: Justin Perona
:Copyright: © 2020 Justin Perona
:License: CC BY-NC 4.0

========================
ECS 154A - Lab 1 WQ 2020
========================

.. contents::
  :local:

Logistics
---------

Submission
~~~~~~~~~~

Due by 20:00 on Monday, 2020-01-20.

Turn in for the Logisim portion is on Gradescope.
Submit the specified .circ files for each problem.
The person submitting should specify their partner's name (if necessary) during the submission process.

Turn in for the survey is on Canvas.
Each person needs to submit a survey, even if they worked with a partner.
More information on the survey is at the end of this document.

Logisim Evolution
~~~~~~~~~~~~~~~~~

We will be using v2.15.0 of `Logisim Evolution`_ for the majority of the quarter.
You can download it here_.

Logisim Evolution is distributed via a JAR file.
JAR files need a Java Runtime Environment (JRE) available to run.
The CSIF has OpenJDK 11 installed already and should work out of the box.
If you want to run it on your own Linux machine, you should be able to find *openjdk11-jre* or something similar via your package manager.
On Windows, I suggest OpenJDK 11 LTS from AdoptOpenJDK_.

Matthew Farrens has a Logisim introduction available on `his website`_; read sections 2 and 3.
Note that this was written for the original Logisim, so some things might look a bit different, but the basics should be the same.
Discussions in the first week will also give a short introduction to Logisim Evolution and how to implement functions.
I'd recommend that you download it before your first discussion so that you can follow along on the tutorial.

.. _`Logisim Evolution`: https://github.com/reds-heig/logisim-evolution
.. _here: https://github.com/reds-heig/logisim-evolution/releases/tag/v2.15.0
.. _AdoptOpenJDK: https://adoptopenjdk.net/
.. _`his website`: http://american.cs.ucdavis.edu/academic/ecs154a/postscript/logisim-tutorial.pdf

Testing
~~~~~~~

**Under construction.**

Grading
~~~~~~~

When you submit your .circ files to Gradescope, an autograder will run each of your circuit files together with my grading circuit for that problem.
If your output matches the expected output for a given problem, you get full credit, otherwise you get a 0 for that problem.
You have unlimited submissions; test as many times as you like.

The autograder expects specific file, circuit, and pin names.
We will provide you with base circuits for each problem (see the *base/* subfolder) that are set up correctly.
**Do not modify the file name, circuit name, or pin names inside Logisim!**
If you do, either your circuit will fail to run or it will error out.
Either way, you'll get a 0.

Constraints
~~~~~~~~~~~

For these problems, you must use designs relying on only basic gates (NOT, AND, OR, NAND, NOR, XOR, XNOR) and the Logisim wiring library, unless specified otherwise.
Violating specified constraints will result in a 0 on the problem in question.
While the autograder may give you credit even if you violate a constraint, we will check submissions after the due date and update grades appropriately.

Logisim Problems [95]
---------------------

1. Quick introduction to Logisim [10]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *lab1problem1.circ*
* Main circuit name: *introduction*
* Input pin(s): *A* [1], *B* [1], *C* [1], *D* [1]
* Output pin(s): *f* [1], *g* [1]

This problem is designed to get you used to Logisim Evolution and how submitting your circuit works on Gradescope.
I *highly recommend* submitting your answer to Gradescope after you finish this part to test that you're doing things correctly.
See the Grading_ section above for more information if you're encountering any problems.

Create two circuits using gates for the following functions.

    f(A, B, C, D) = AC + B!D + !C!D

    g(A, B, C, D) = !A!D + A!BD + B!CD + ABCD

After opening the base circuit for this problem, you will be greeted by some input and output pins and nothing else.
The basic gates are on the top toolbar, or you can open the Gates library in the left sidebar.

I highly recommend using tunnels, and continuing to use them throughout the rest of the labs.
Tunnels make your circuit cleaner and allows for easier debugging; they allow you to move a value from one part of the circuit to another without having to drag a wire all the way across.
You can create tunnels for all the inputs (ABCD) and their complements.
Instead of hooking up the inputs directly to the gates, you can hook up duplicates of the tunnels instead.

Once you're finished with a circuit and want to test it manually, you can use the hand tool and click on the input pins to change their values, which will propagate to the rest of the circuit.
For other methods of testing, see the Testing_ section above.
You can reset the simulation back to the start with Ctrl-R to test again after you make changes.

2. Minterm [10]
~~~~~~~~~~~~~~~

* Submission file for this part: *lab1problem2.circ*
* Main circuit name: *minterm*
* Input pin(s): *fourbitinput* [4]
* Output pin(s): *h* [1]

Implement the minterm m_14 for a 4 bit input.
You will need to learn how to use a splitter to access the individual bits.

You may not use OR nor NOR gates for this problem.

3. Maxterm [10]
~~~~~~~~~~~~~~~

* Submission file for this part: *lab1problem3.circ*
* Main circuit name: *maxterm*
* Input pin(s): *fourbitinput* [4]
* Output pin(s): *j* [1]

Implement the maxterm M_6 for a 4 bit input.

You may not use AND nor NAND gates for this problem.

4. Karnaugh map [10]
~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *lab1problem4.circ*
* Main circuit name: *karnaugh*
* Input pin(s): *fourbitinput* [4]
* Output pin(s): *k* [1]

Derive and implement a minimum sum-of-products expression for the following function:

    k(fourbitinput) = m0 + D2 + m4 + m6 + D7 + D8 + m10 + m13 + m14

m stands for minterm, and D stands for don't care.

5. Single-digit seven-segment display [35]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *lab1problem5.circ*
* Main circuit name: *singledigit*
* Input pin(s): *i* [4]
* Output pin(s): *a* [1], *b* [1], *c* [1], *d* [1], *e* [1], *f* [1], *g* [1]

Given the following binary-coded-decimal to seven-segment display code converter, derive minimal sum-of-products expressions for the outputs *a*, *b*, *c*, *d*, *e*, *f*, and *g* of the seven-segment display.
Implement the resulting circuits.

.. image:: seven-segment-display.png
    :width: 50%
    :align: center

====== ====== ====== ====== = === === === === === === ===
**i3** **i2** **i1** **i0** | *a* *b* *c* *d* *e* *f* *g*
0      0      0      0      | 1   1   1   1   1   1   0
0      0      0      1      | 0   1   1   0   0   0   0
0      0      1      0      | 1   1   0   1   1   0   1
0      0      1      1      | 1   1   1   1   0   0   1
0      1      0      0      | 0   1   1   0   0   1   1
0      1      0      1      | 1   0   1   1   0   1   1
0      1      1      0      | 1   0   1   1   1   1   1
0      1      1      1      | 1   1   1   0   0   0   0
1      0      0      0      | 1   1   1   1   1   1   1
1      0      0      1      | 1   1   1   1   0   1   1
====== ====== ====== ====== = === === === === === === ===

The 3rd and most significant bit of the input *i* corresponds to **i3** on the table.
Similarly, the 0th and least significant bit of the input *i* corresponds to **i0** on the table.
We will use this naming system throughout the class.

Testing this problem is best done manually by attaching the relevant inputs to the *7-Segment Display* module from the Input/Output library of Logisim.
Feel free to leave it inside your circuit if you want before submission; it won't affect the testing.

6. 4-to-1 multiplexor [20]
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *lab1problem6.circ*
* Main circuit name: *multiplexor*
* Input pin(s): *inputzero* [3], *inputone* [3], *inputtwo* [3], *inputthree* [3], *selector* [2]
* Output pin(s): *muxoutput* [3]

Create a 4-to-1 multiplexer that uses three data bits.
The *selector* input chooses between which of the four *input* pins to output to *muxoutput*.
Hint: the lecture notes show how to make a 4-to-1 multiplexor with one data bit, but you'll need to figure out what to modify to support more data bits.

You may not use MUXes for this problem as it defeats the purpose of the problem.

Extra credit: Triple-digit display [15]
---------------------------------------

* Submission file for this part: *lab1extracredit.circ*
* Main circuit name: *tripledigit*
* Input pin(s): *thousand* [10]
* Output pin(s): *hundreds* [7], *tens* [7], *ones* [7]

This extra credit problem builds upon problem 5.
Using your circuits from problem 5, build a triple-digit display that can display numbers between 0 and 999.
The input number to display is provided in *thousand*.
Note that *thousand* is 10 bits and thus has a maximum of 1024; numbers higher than 999 won't be tested so you may ignore them.

For the output pins, concatenate your values for *a*, *b*, *c*, *d*, *e*, *f*, and *g* in that order for each relevant digit.
Thus, the 6th and most significant bit should be your *a* output for that digit, while the 0th and least significant bit should be your *g* output for that digit.

The image below shows an example of how the circuit works for an input value of 36.

.. image:: triple-digit-display.png
    :width: 50%
    :align: center

You may use anything in the Logisim Arithmetic library for this problem.
Testing this problem is best done manually by attaching relevant inputs to *7-Segment Display* modules from the Input/Output library of Logisim.
Feel free to leave them inside your circuit if you want before submission; they won't affect the testing.

Survey [5]
----------

For every lab, there will be an associated survey worth 5% of the grade.
This survey is going to ask you about how you felt about the assignment and how much time you spent on it.
Everybody needs to submit a survey response individually.

You can find the survey on Canvas_.
There's no late penalty on the survey portion.
As long as you submit by the late submission deadline, you'll get full credit.

.. _Canvas: https://canvas.ucdavis.edu
