# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid += payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    print(month, round(total_paid, 2), principal)

print(f'The number of months taken to pay was {month}, with the total amount paid being ${round(total_paid, 2)}')
