# The Number Partitioning Problem

The number partitioning problem begins with a set of numbers, S.  We must split
the set of numbers into two sets with equal sum.  In our training course, we
discuss this problem and how to create a QUBO to solve it.

In this exercise, you are given an Ocean program outline and must create
the QUBO dictionary (Q) that is provided to the D-Wave QPU and choose
appropriate values for `chainstrength` and `numruns`.

To run your program type `python npp.py`.  You have successfully completed the
exercise when you are able to see output showing S0 sum and S1 sum are both
equal to 83.

To complete the program, please complete the following:

- Add your token to the `get_token` function.
- Fill in the entries in your QUBO dictionary in the `get_qubo` function. In your QUBO dictionary use 0-7 for the variables.
- Find good values for `chainstrength` and `numruns` in the `run_on_qpu`
   function.

If you get stuck, you can first check that your QUBO is correct by setting
`chainstrength = None` on line 47 in `npp.py`.  This will use the Ocean chain
strength tuning tool, and set the chain strength for you.

## License

Released under the Apache License 2.0. See [LICENSE](LICENSE) file.
