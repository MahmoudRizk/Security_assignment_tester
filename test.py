import subprocess
from subprocess import call
import random
import sys
from time import sleep
"""
#call(['g++', 'main.cpp', '-std=c++11', '-O2'])  #build c++ from here.

#////////////////////////////////////////////////////////////////////////////#
test_cases = 5000   #number of test cases.
P_bits = 16         #[0-9] bits.
Q_bits = 16         #[0-9] bits.
E_bits = 16         #[0-9] bits.
test_in_detail = False  # print details of each test case.

def Algorithm(p,q,e): ## Algorithm being tested in c++.
    return p+q
    #return p-q
    #return p/q
    #return pow(p,q,e)
#/////////////////////////////////////////////////////////////////////////////#
"""
def test(test_cases, P_bits, Q_bits, E_bits, test_in_detail, Algorithm, c_file_name):
    error_flag = False
    for i in range(test_cases):
        p = random.getrandbits(P_bits)
        q = random.getrandbits(Q_bits)
        e = random.getrandbits(E_bits)

        while q==0 or q==1  or e==0:
            q = random.getrandbits(Q_bits)
        while e==0:
            e = random.getrandbits(E_bits)

        if(test_in_detail):
            print 'test_no.:', i
            print "p:", p
            print "q:", q
            print "e:", e

        raw = subprocess.check_output(['./' + c_file_name,str(p),str(q),str(e)])
        output = raw.split()[0]
        difference = int(output) - Algorithm(p,q,e)

        if difference != 0:
            error_flag = True
            break

        if(i%(test_cases/10)==0 and not test_in_detail):
            print 'test_no:', i

        if(test_in_detail):
            sleep(0.5)

    if(not error_flag):
        print 'test_no:', test_cases
        print 'Succeeded (^_^)'
    else:
        print "Error, test_no.:" , i
        print 'p:', p
        print 'q:', q
        print "C++_output:", output
        print "Python    :", Algorithm(p,q,e)
        print 'Difference:', difference
