#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:33:02 2017

@author: Juan
"""

def getSavings( rate, salary ):
    goal = 250000
    r = .04
    semi_annual_raise = .07
    month_salary = salary/12.0
    deposit = float(month_salary) * rate
    savings = 0
    for i in range(1, 36):
        gain = (savings * r) / 12.0
        savings = savings + gain + deposit
        if i % 6 == 0:
            deposit = deposit + (semi_annual_raise * deposit)
    if DEBUG_MODE:
        print (goal, savings, rate)
    return savings
    
### Main ###
DEBUG_MODE = False

low = 0
high = 10000
divisor = 10000.0
ans = (low + high) / 2.0
steps = 0
target = 250000
epsilon = 100
annual_salary = float(input("Enter the starting salary: "))

if getSavings( 1, annual_salary) > target:
    while abs(float(getSavings((ans/divisor), annual_salary) - target)) > epsilon:
        steps = steps + 1
        if DEBUG_MODE:
            print (steps, "low =", low, " and high =", high, " and ans =", ans/divisor)
        if getSavings((ans/divisor), annual_salary) > target:
            high = ans
        else:
            low = ans

        ans = (low + high) / 2.0

    print ("Best rate is: ", ans/divisor)
    print ("Number of steps: ", steps)
else:
    print ("You cannot achieve your goals with that salary.  Have you considered skilling up with OpenCourseWare?")

