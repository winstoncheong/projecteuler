#!/usr/bin/env python

# Title: Largest palindrome product
# Description: Find the largest palindrome made from the product of two 3-digit numbers

from common import is_palindrome
from sys import exit

largest = 1
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if i*j > largest and is_palindrome(i*j):
            largest = i*j

print largest
