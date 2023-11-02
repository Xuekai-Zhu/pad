def solution():
    """Tara has been planning to buy a laptop which costs $1000. A computer shop accepts payment in installments of $65 per month provided that a 20% down payment is made. If Tara wants to pay an additional $20 for the down payment, how much will her balance be after paying for 4 months?"""
    # Define the total cost of the laptop
    total_cost = 1000

    # Calculate the down payment
    down_payment = total_cost * 0.2 + 20

    # Calculate the remaining balance
    remaining_balance = total_cost - down_payment

    # Calculate the balance after 4 monthly payments
    monthly_payment = 65
    for i in range(4):
        remaining_balance -= monthly_payment

    result = remaining_balance
    return result

print(solution())