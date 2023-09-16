#! /usr/bin/env python3

import sympy

expr = "x**2 + x + b"

expr = sympy.parsing.sympy_parser.parse_expr(expr)

print(expr)

sol = sympy.solve(expr, 'x')

print(sol)
