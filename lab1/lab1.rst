:Author: Justin Perona
:Copyright: © 2020 Justin Perona

========================
ECS 154A - Lab 1 WQ 2020
========================

.. contents:: **Table of Contents**

Logistics
---------

Submission
~~~~~~~~~~

Due by 20:00 on Friday, 2020-01-17.

Turn in for the Logisim portion is on Gradescope.
Submit the specified .circ files for each problem.
The person submitting should specify their partner's name (if necessary) during the submission process.

Turn in for the survey is on Canvas.
Each person needs to submit a survey, even if they worked with a partner.
More information on the survey is at the end of this document.

Logisim Evolution
~~~~~~~~~~~~~~~~~

.. _`Logisim Evolution`: https://github.com/reds-heig/logisim-evolution
.. _here: https://github.com/reds-heig/logisim-evolution/releases/tag/v2.15.0
.. _AdoptOpenJDK: https://adoptopenjdk.net/
.. _`his website`: http://american.cs.ucdavis.edu/academic/ecs154a/postscript/logisim-tutorial.pdf

We will be using v2.15.0 of `Logisim Evolution`_ for the majority of the quarter.
You can download it here_.

Logisim Evolution is distributed via a JAR file.
JAR files need a Java Runtime Environment (JRE) available to run.
The CSIF has OpenJDK 11 installed already and should work out of the box.
If you want to run it on your own Linux machine, you should be able to find *openjdk11-jre* or something similar via your package manager.
On Windows, I suggest OpenJDK 11 LTS from AdoptOpenJDK_.

Matthew Farrens has a Logisim introduction available on `his website`_.
Read everything up to section 3; you can ignore section 4 for now.
Discussions in the first week will also give a short introduction to Logisim Evolution and how to implement functions.
I'd recommended that you download it before your first discussion so that you can follow along on the tutorial.

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

For these problems, you must use designs relying on only AND gates, OR gates, XOR gates, NOT gates, MUXes, decoders, and the Logisim wiring library, unless specified otherwise.
Violating this constraint will result in a 0 on the problem in question.

Logisim Problems [95]
---------------------

1. Quick introduction to Logisim [10]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Submission file for this part: *lab1problem1.circ*
* Main circuit name: *problem1*
* Input pins: *A*, *B*, *C*, *D*
* Output pins: *f*, *g*

This problem is designed to get you used to Logisim Evolution and how submitting your circuit works on Gradescope.
I *highly recommend* submitting your answer to Gradescope after you finish this part to test that you're doing things correctly.
See the Grading_ section above for more information on how your circuit is graded or if you're encountering any problems.

Create two circuits using gates for the following functions.
You may not use a MUX for this problem.

    f(A, B, C, D) = !A!D + A!BD + B!CD + ABCD

    g(A, B, C, D) = AC + B!D + !C!D

After opening the base circuit for this problem, you will be greeted by some input and output pins and nothing else.
The basic gates are on the top toolbar, or you can open the Gates folder in the left sidebar.

I highly recommend using tunnels, and continuing to use them throughout the rest of the labs.
It allows you to move a value from one part of the circuit to another without having to drag a wire all the way across.
You can create tunnels for all the inputs (ABCD) and their complements.
Instead of hooking up the inputs directly to the gates, you can hook up duplicates of the tunnels instead.

Once you're finished with a circuit and want to test it, you can use the hand tool and click on the input pins to change their values, which will propagate to the rest of the circuit.
We will talk about other methods for testing later in the quarter.
You can reset the simulation back to the start with Ctrl-R to test again after you make changes.

2. []
~~~~~

3. []
~~~~~

4. []
~~~~~

5. Single-digit seven-segment display [30]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

6. Three-digit display [15]
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Survey [5]
----------

For every lab, there will be an associated survey worth 5% of the grade.
This survey is going to ask you about how you felt about the assignment and how much time you spent on it.
Everybody needs to submit a survey response individually.

You can find the survey on Canvas.
There's no late penalty on the survey portion.
As long as you submit by the late submission deadline, you'll get full credit.
