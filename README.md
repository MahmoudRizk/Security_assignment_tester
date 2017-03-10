# Security_assignment_tester

## How it works ?
- Python script generats 3 random number then run the c++ binaries.The script waits for the output of the c++ algorithm and  compares it with same algorithm implemented in python. <br>
- Run on __Linux__  OS only.

## How to launch it ?
1) Build .cpp file.
```
g++ main.cpp -std=c++11 -o binaries.out
```
2)  Run the python script.
```
python __main__.py binaries.out
```
#### Note: 
- The numbers sent to the c++ are in string datatype, so needed to be converted. <br>
- The c++ program must output the result to be compared only.
- All running files must be in the same directory.

## How to make your own test ?
- Edit the __Algorithm()__ function in ``` __main__.py ```, and write your custom algorithm.

```python
def Algorithm(p,q,e): 
    return p+q          #Addition
```
- Bits of the random number generated can be cahnged in ```__main__.py``` file.


