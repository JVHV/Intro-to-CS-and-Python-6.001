#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:33:02 2017

@author: Juan
"""

annual_salary= float (input("What is your annual salary?"))

portion_saved=float(input("How much are you going to save from your salary (decimal)?"))

total_cost= float(input("What is the price of your dream house?"))

semi_annual_raise= float(input("How much is going to be your semi-annual raise?(decimal percentage)"))

r=0.04

current_savings=0 

portion_down_payment= total_cost*0.25

monthly_salary =float(annual_salary / 12)

deposit = float(monthly_salary * portion_saved)

months=0



while current_savings < portion_down_payment:
    gain=(current_savings*r)/12
    current_savings+= gain +deposit
    months= months + 1
    if months %6== 0:
        deposit= deposit + (semi_annual_raise*deposit)

    
     
    
print (current_savings, months)    



