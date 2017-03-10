from test import test
import sys
from subprocess import call

#call(['g++', 'main.cpp', '-std=c++11', '-O2'])  #build c++ from here.

test_cases = 5000   #number of test cases.
P_bits = 16         #[0-9] bits.
Q_bits = 16         #[0-9] bits.
E_bits = 16         #[0-9] bits.
test_in_detail = False  # print details of each test case.
c_file_name = sys.argv[1]

def Algorithm(p,q,e): ## Algorithm being tested in c++.
    return p+q          #Addition
    #return p-q         #Subtraction
    #return p/q         #Division
    #return pow(p,q,e)  #power_mod (p^q)%e

test(test_cases, P_bits, Q_bits, E_bits, test_in_detail, Algorithm, c_file_name)
