def solution():
    """Tara has been planning to buy a laptop which costs $1000. A computer shop accepts payment in installments of $65 per month provided that a 20% down payment is made. If Tara wants to pay an additional $20 for the down payment, how much will her balance be after paying for 4 months?"""
    laptop_cost = 1000
    down_payment_percentage = 20
    down_payment = laptop_cost * (down_payment_percentage / 100) + 20
    balance = laptop_cost - down_payment
    monthly_payment = 65
    total_payment_after_4_months = monthly_payment * 4
    remaining_balance = balance - total_payment_after_4_months
    result = remaining_balance
    return result

print(solution())