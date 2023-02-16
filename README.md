# Maquina_Estados_Finitos

Algorithm that implements a finite state machine to validate expressions.


## In-depth explanation:

This program, when executed, will determine whether an
input is part of the language 𝐿 defined by 𝐿 = {𝑥 | 𝑥 ∈
{𝑎,𝑏}∗ 𝑒 each 𝑎 in 𝑥 is followed by at least two 𝑏} according to the alphabet Σ={{𝑎,𝑏,𝑐}.


The program you will develop will receive as input a text file (.txt)
containing several strings. The first line of the file indicates how many strings are in the input text file. The subsequent lines contain one string per line. The following is an example of the lines that may exist in a test file for the program you are going to develop:


3 

abbaba 

abababb 

bbabbaaab 



In this example we have 3 input strings. The number of strings in each file will be represented by a positive integer. Your program's response must contain one, and
only one output line for each string. These lines will contain the input string and the result validation result in the following format:


abbaba: does not belong.


The output can be sent to a text file, or to the standard terminal, and will be of one output line per input string. In the case of the example, we will have 3 lines of output.
For your program to be tested you must create at least three input files files containing a different number of different strings.

