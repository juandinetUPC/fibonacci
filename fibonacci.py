"""
Metodos de generacion de numeros fibonacci
by: Juan Diego Cubillos - Especialista en ingenieria de software
"""
#python imports
from itertools import count
from time import time

def fibonacci(n):
    """generate the Nth fibonacci number, using a traditional recursive method"""
    # 0 1 1 2 3 5 8 13 21
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_M(n , memo = {}):
    """generate the Nth fibonacci number using a memoization method"""
    # 0 1 1 2 3 5 8 13 21
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_M(n-1, memo) + fibonacci_M(n-2, memo)
    return memo[n]    


def main():
    runtimes = {}
    percent_acc=0
    # we will use a advanced range to generate the fibonacci numbers
    begin = 25
    end = 30
    
    # generation of fibonacci numbers using a traditional recursive method
    for idx in range(begin, end):
        start_time = time()
        fibonacci(idx) # call the fibonacci function
        runtime = time() - start_time # calculate the runtime
        print (idx, f"-- Runtime {runtime:.3f} seconds --")
        runtimes[idx] = runtime
        
    average_percent_increase = 0
    for idx in range(begin, end): # calculate the average percentage increase
        if idx == begin:
            continue
    # calculate the average runtime
        percent = (((runtimes[idx] - runtimes[idx-1])*100) / runtimes[idx - 1])
        percent_acc += percent
    average_percent_increase =  (percent_acc / (len(runtimes)-1) )
    print(f"Average  percent increase: {average_percent_increase:.3f} %")
    
    
    # test method_name = "fibonacci_M" using memoization
    print("\n\n Fibonacci using memoization")
    for i in range(100 + 1): # we can generate the fibonacci numbers up to 38 (500 for example)
        start_time = time()
        print(fibonacci_M(i), end=" ") # call the fibonacci_M function
        # print(fibonacci(i), end=" ") # call the fibonacci traditional function
        runtime = time() - start_time
        print (i, f"--Runtime {runtime:.3f} seconds --")
    
    
        
        
if __name__ == "__main__":
    main()