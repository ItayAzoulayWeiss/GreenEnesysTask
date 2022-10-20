import numpy as np
import numpy_financial as npf
import pandas as pd

#Q1
income = []
expenses = []
rent  = 2300
pet_fee = 50
mortage = 1120
property_taxes = 430
insurance = 75
pmi = 100
hoa = 100
property_management = 20
ongoing_maintenance = 115

income.extend((rent,pet_fee))
expenses.extend((mortage,property_management,property_taxes,insurance,pmi,hoa,ongoing_maintenance))

monthly_cashflow = sum(income)-sum(expenses)

print(f'Monthly Cashflow : {monthly_cashflow}\n')
#Q2
yearly_cashflow = monthly_cashflow*12
investment = -100000

IRR = npf.irr([investment,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow-investment])

rate = yearly_cashflow/(-investment)
NPV = npf.npv(rate,[investment,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow,yearly_cashflow-investment])

payback = (-investment)/yearly_cashflow

print(f'IRR : {IRR}\nNPV : {NPV}\nPayback : {payback}\n')


#Q3
from scipy.stats import norm
import time
import math

rent_var=np.random.normal(2650,350,1000)
lst=np.round(rent_var)
x=0
start = time.time()

for i in lst:
    ycs = (i+pet_fee-sum(expenses))*12
    irr = npf.irr([investment,ycs,ycs,ycs,ycs,ycs,ycs,ycs,ycs,ycs,ycs-investment])
    if irr>=0.04:
        x+=1

end = time.time()
log_time = math.log((end-start))
print(f'From 1000 random rent amounts from the following distribution, {x/1000}% the assets IRR was bigger than 4%.\nwhich means that given that the asset does not match the customers conditions of 5% rist tolerance\n\nthe log of the time the procces took is {log_time}')

