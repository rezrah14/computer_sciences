import time
import matplotlib.pyplot as plt


def fib_1(nn):
    if nn <= 3:
        return 1
    f = fib_0(nn - 1) + fib_0(nn - 2)
    return f


def fib_2(nn, memo=None):
    if memo is None:
        memo = {1: 0, 2: 1}
    if nn in memo:
        return memo[nn]
    f = fib_1(nn - 1, memo) + fib_1(nn - 2, memo)
    memo[nn] = f
    return f


def fib_2(nn):
    a = 0
    b = 1
    if nn == 1:
        pass
        #print(a)
    else:
#
        for i in range(2, nn):
            c = a + b
            a = b
            b = c
            #print(c)
    return c


if __name__ == "__main__":
    res = {0: [], 1: [], 2: []}
    for num in range(10, 35):
        start = time.time()
        fib_n = fib_0(num)
        end = time.time()
        res[0].append((num, (end - start) * 1000))

        start = time.time()
        fib_n = fib_1(num)
        end = time.time()
        res[1].append((num, (end - start) * 1000))

        start = time.time()
        fib_n = fib_2(num)
        end = time.time()
        res[2].append((num, (end - start) * 1000))

    x_vals = [num for num in range(10, 35)]
    y_vals = [item[1] for item in res[0]]
    plt.plot(x_vals, y_vals, label='fib_0')
    y_vals = [item[1] for item in res[1]]
    plt.plot(x_vals, y_vals, label='fib_1')
    y_vals = [item[1] for item in res[2]]
    plt.plot(x_vals, y_vals, label='fib_2')

    # Add labels and title
    plt.title("Fibonacci")
    plt.xlabel("Number")
    plt.ylabel("Time(milli sec)")
    plt.legend()
    #plt.show()

    print("Done!")


