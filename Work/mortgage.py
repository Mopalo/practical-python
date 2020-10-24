# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra = 1000

while month <= 12:
    principal = principal * (1+rate/12) - (payment + extra)
    total_paid = total_paid + (payment + extra)
    month += 1

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month += 1

print('Months taken', month)
print('Total paid', total_paid)
