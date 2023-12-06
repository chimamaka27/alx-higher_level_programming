#!/usr/bin/python3
#include <Python.h>

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (long int i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
        {
            print_python_bytes(item);
        }
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    char *str = PyBytes_AsString(p);
    long int size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
    for (long int i = 0; i < size + 1 && i < 10; i++)
    {
        printf("%02hhx", str[i]);
        if (i < 9 && i < size)
        {
            printf(" ");
        }
    }
    printf("\n");
}
