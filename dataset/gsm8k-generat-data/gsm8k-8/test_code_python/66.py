def solution():
    # Define the cost of the laptop and the down payment
    laptop_cost = 1000
    down_payment = 0.2 * laptop_cost + 20

    # Calculate the remaining balance after the down payment
    remaining_balance = laptop_cost - down_payment

    # Calculate the monthly installment
    monthly_installment = 65

    # Calculate the balance after 4 months of payments
    balance_after_4_months = remaining_balance - 4 * monthly_installment
    result = balance_after_4_months
    return result

print(solution())