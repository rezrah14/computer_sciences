# Fibonacci

Probably some general concepts of `computer sciences` can be explained in the simplest form using this example.
Generating `n` terms of [Fibonacci serries](https://en.wikipedia.org/wiki/Fibonacci_number) seems a trivial task. 
However, it can be used to show how the poor implementation of any algorithm even for such a trivial problem could 
end up with scalability issues (in time and space or both).

## 1. Recursive Call - Brute Force Approach
The following implementation would be probably the first algorithm in your mind. 
Nothing is wrong with it! However, the exponential nature of the recursive calls will show up as a serious scalability 
problem for higher number of terms (`n`) in Fibonacci series! 

```
def fib_1(n):
    if n < 2:
        return n
    f = fib_0(n - 1) + fib_0(n - 2)
    return f
```
<p align="center">
    <img src="./fib_rec.png" width="350" height="300" align="center">
</p>

## 2. Dynamic Programming - memory caching
In the previous approach, as you can see there are lots of redundant duplicated calculations. Let's store the calculated
values and use them in the recursive calls. Here, we have used a dictionary data structure (`O(1)` in accessing elements).
This has huge impact on the performance. Now, it is possible to calculate the terms of Fibonacci sequence even for very 
large number very fast! However, this speed is not granted for free! we have to memorized lots of values in memory.
Could we do better and consume less memory without degrading the performance!?

```
def fib_2(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1, 2:1}
    if n in memo:
        return memo[n]
    f = fib_2(n - 1, memo) + fib_2(n - 2, memo)
    memo[n] = f
    return f
```

## 3. Optimal Solution
The previous approaches are top-bottom approaches. Let's change the calculations to start from bottom and go higher until 
reaching the `nth` term of Fibonacci sequence! This way, there is no need to store the calculated values! it is required to
keep track of only the most two recent values. Besides, this approach allows easily to print the entire sequence if requested.

```
def fib_3(n):
    a = 0
    b = 1
    if n <= 1:
        pass
        #print(a)
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            #print(c)
    return c
```

<p align="center">
    <img src="./time.png" width="600" height="600" align="center">
</p>