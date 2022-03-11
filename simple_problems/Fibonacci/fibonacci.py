import time
import matplotlib.pyplot as plt


def fib_1(n):
    if n <= 3:
        return 1
    f = fib_1(n - 1) + fib_1(n - 2)
    return f


def fib_2(n, memo=None):
    if memo is None:
        memo = {1: 0, 2: 1, 3: 1}
    if n in memo:
        return memo[n]
    f = fib_2(n - 1, memo) + fib_2(n - 2, memo)
    memo[n] = f
    return f


def fib_3(n):
    a = 0
    b = 1
    # print(0)
    # print(1)
    if n == 1:
        pass
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            # print(c)
    return c


if __name__ == "__main__":
    res = {0: [], 1: [], 2: []}
    for num in range(10, 35):
        start = time.time()
        fib_n = fib_1(num)
        end = time.time()
        res[0].append((num, (end - start) * 1000))

        start = time.time()
        fib_n = fib_2(num)
        end = time.time()
        res[1].append((num, (end - start) * 1000))

        start = time.time()
        fib_n = fib_3(num)
        end = time.time()
        res[2].append((num, (end - start) * 1000))

    x_vals = [num for num in range(10, 35)]
    y_vals = [item[1] for item in res[0]]
    plt.plot(x_vals, y_vals, label='fib_1')
    y_vals = [item[1] for item in res[1]]
    plt.plot(x_vals, y_vals, label='fib_2')
    y_vals = [item[1] for item in res[2]]
    plt.plot(x_vals, y_vals, label='fib_3')

    # Add labels and title
    plt.title("Fibonacci")
    plt.xlabel("Number")
    plt.ylabel("Time(milli sec)")
    plt.legend()
    #plt.show()

    print("Done!")


