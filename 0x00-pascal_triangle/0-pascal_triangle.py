#!/usr/bin/python3
"""Pascals Triangle."""

def pascal_triangle(n):
    """Define pascal triangle."""
    if n <= 0:
        return []
    else:
        ls = []
        ls.append([1])

        if n == 1:
            return ls

        for i in range(1, n):
            current = [1]
            prev_list = ls[i - 1]

            for j in range(1, i):
                new = prev_list[j-1] + prev_list[j]
                current.append(new)
            current.append(1)
            ls.append(current)
    return ls
