#! /usr/bin/env python3

import sympy

sympy.init_printing()

class B(sympy.NumberSymbol): # class SymbolTrick(sympy.NumberSymbol):
    def __new__(self, name):
        obj = sympy.NumberSymbol.__new__(self)
        obj._name = name
        return obj

    _as_mpf_val = sympy.pi._as_mpf_val
    approximation_interval = sympy.pi.approximation_interval
    __str__ = lambda self: str(self._name)

class A(B): pass
class C(B): pass
class D(B): pass

def generate_tylor(f, evaluate_at, num_terms):
    x = sympy.symbols('x')
    c = sympy.symbols('c')

    current_derivative = f.subs(x, c)
    multiplicator = x - c

    p = 0
    for idx in range(num_terms):
        p += current_derivative * multiplicator**idx / sympy.factorial(idx)
        current_derivative = sympy.diff(current_derivative)

    return p.subs(c, evaluate_at)

# a, b, c, d = sympy.symbols('a b c d')
x = sympy.symbols('x')

a = A('a')
b = B('b')
c = B('c')
d = B('d')

f = a*x**3 + b*x**2 + c*x + d

cubic_solutions = sympy.solve(f, x)

for solution in cubic_solutions:
    print(solution)
    print()
    tylor = solution.series(x0=1, n=68).removeO()
    # tylor = generate_tylor(solution, 1, 1)
    print(tylor)
    print()
    print()
    print()
    print()

# breakpoint()
