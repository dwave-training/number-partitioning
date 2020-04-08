# number-partitioning
Number partitioning problem coding exercise.

The number partitioning problem begins with a set of numbers, S.  We must split the set of numbers into two sets with equal sum.  In our training course, we discuss this problem and how to create a QUBO to solve it.

In this exercise, students are given an Ocean program outline and must create the QUBO dictionary (Q) that is provided to the D-Wave QPU and choose appropriate values for `chainstrength` and `numruns`.

To run your program type `python npp.py`.  Uncomment the last line in the program to see output displaying the sums of the two sets, S0 and S1, returned by the QPU, followed by the list of numbers in set S0.  

You have successfully completed the exercise when you are able to see output showing S0 sum and S1 sum are both equal to 83.