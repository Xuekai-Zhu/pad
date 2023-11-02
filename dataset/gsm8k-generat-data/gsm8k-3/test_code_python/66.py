def solution():
    """Tara has been planning to buy a laptop which costs $1000. A computer shop accepts payment in installments of $65 per month provided that a 20% down payment is made. If Tara wants to pay an additional $20 for the down payment, how much will her balance be after paying for 4 months?"""
    # Define the cost of the laptop
    laptop_cost = 1000

    # Define the down payment amount and calculate the total amount to be financed
    down_payment = laptop_cost * 0.2 + 20
    financed_amount = laptop_cost - down_payment

    # Calculate the monthly payment amount and the balance after 4 months
    monthly_payment = 65
    balance_after_4_months = financed_amount - monthly_payment * 4

    # Return the result
    result = balance_after_4_months
    return result

print(solution())