import timeit
import PyCPBoost  

def python_add(a, b):
    return a + b

def python_multiply(a, b):
    return a * b

def python_heavy_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

a, b = 10000, 20000
N_TIMES = 10_000_000  
N = 10_000_000

setup_py_add = f"from __main__ import python_add, a, b"
stmt_py_add = "python_add(a, b)"

py_time_add = timeit.timeit(stmt=stmt_py_add, setup=setup_py_add, number=N_TIMES)
print(f"Pure Python FUNC ADD: {py_time_add:.6f} วินาที")

setup_cpp_add = f"from __main__ import PyCPBoost, a, b"
stmt_cpp_add = "PyCPBoost.add(a, b)"

cpp_time_add = timeit.timeit(stmt=stmt_cpp_add, setup=setup_cpp_add, number=N_TIMES)
print(f"C++ Extension FUNC ADD: {cpp_time_add:.6f} วินาที")

setup_py_multiply = f"from __main__ import python_multiply, a, b"
stmt_py_multiply = "python_multiply(a, b)"

py_time_multiply = timeit.timeit(stmt=stmt_py_multiply, setup=setup_py_multiply, number=N_TIMES)
print(f"Pure Python FUNC MULYIPLY: {py_time_multiply:.6f} วินาที")

setup_cpp_multiply = f"from __main__ import PyCPBoost, a, b"
stmt_cpp_multiply = "PyCPBoost.multiply(a, b)"

cpp_time_multiply = timeit.timeit(stmt=stmt_cpp_multiply, setup=setup_cpp_multiply, number=N_TIMES)
print(f"C++ Extension FUNC MULYIPLY: {cpp_time_multiply:.6f} วินาที")

py_time = timeit.timeit(f"python_heavy_loop({N})", 
                        setup="from __main__ import python_heavy_loop", 
                        number=10)
print(f"Python heavy loop: {py_time / 10:.6f} วินาที")

cpp_time = timeit.timeit(f"PyCPBoost.heavy_loop({N})", 
                         setup="import PyCPBoost", 
                         number=10)
print(f"C++ heavy loop:    {cpp_time / 10:.6f} วินาที")