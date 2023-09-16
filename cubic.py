#! /usr/bin/env python3

# NOTE
#
#sympy.pprint(sympy.solve(f, z))

import sympy

sympy.init_printing(use_unicode=True)
#sympy.init_printing()

a, b, c = sympy.symbols('a b c')
z = sympy.symbols('z')

f = a*z**2 + b*z + c

f /= a
f = sympy.expand(f)

d = sympy.symbols('d')
x = sympy.symbols('x')
f = f.subs(z, x - d)
f = sympy.expand(f)

# collect all terms that contain `z**1`
f2 = sympy.collect(f, x, evaluate=False)[x]
# solve
f2 /= -2
assert len(f2.args) == 2
assert f2.args[0] == d
f2_sol = -f2.args[1]
# # put solution back in equasion
f = f.subs(d, f2_sol)

d = None

# solve `y`


sympy.pprint(f)

breakpoint()