long long cpp_fast_add(long long a, long long b){
    return a + b;
}

double cpp_fast_multiply(double a, double b){
    return a * b;
}

long long cpp_heavy_loop(long long n) {
    long long total = 0;
    for (long long i = 0; i < n; ++i) {
        total += i;
    }
    return total;
}

extern "C"{
    #include <Python.h>

    static PyObject* py_fast_add(PyObject* self, PyObject* args){
        long long a, b;
        if( !PyArg_ParseTuple(args, "LL", &a, &b)){
            return NULL;
        }

        long long result = cpp_fast_add(a, b);

        return PyLong_FromLongLong(result);
    }

    static PyObject* py_fast_multiply(PyObject* self, PyObject* args){
        double a, b;
        if( !PyArg_ParseTuple(args, "dd", &a, &b)){
            return NULL;
        }

        double result = cpp_fast_multiply(a, b);

        return PyFloat_FromDouble(result);
    } 

    static PyObject* py_heavy_loop(PyObject* self, PyObject* args) {
        long long n;
        if (!PyArg_ParseTuple(args, "L", &n)) return NULL; 

        long long result = cpp_heavy_loop(n); 

        return PyLong_FromLongLong(result);
    }
    
    static PyMethodDef MyModuleMethods[] {
        {"add", py_fast_add, METH_VARARGS, "Add two number using C++"},
        {"multiply", py_fast_multiply, METH_VARARGS, "Multiply two number using C++"},
        {"heavy_loop", py_heavy_loop, METH_VARARGS, "Run a heavy loop in C++"},
        {NULL, NULL, 0, NULL}
    };

    static struct PyModuleDef first_extension
    {
        PyModuleDef_HEAD_INIT,
        "first_extension",
        "a simple C++ extension example",
        -1,
        MyModuleMethods
    };

    PyMODINIT_FUNC PyInit_first_extension(void){
        return PyModule_Create(&first_extension);
    }
}