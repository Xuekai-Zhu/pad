def solution():
    """Tara has been planning to buy a laptop which costs $1000. A computer shop accepts payment in installments of $65 per month provided that a 20% down payment is made. If Tara wants to pay an additional $20 for the down payment, how much will her balance be after paying for 4 months?"""
    laptop_cost = 1000
    down_payment = laptop_cost * 0.2 + 20
    balance = laptop_cost - down_payment
    monthly_installment = 65
    remaining_months = 4
    for i in range(remaining_months):
        balance -= monthly_installment
    result = balance
    return result

print(solution())