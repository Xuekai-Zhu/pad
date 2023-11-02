def solution():
    laptop_cost = 1000  # cost of laptop
    down_payment = (20/100) * laptop_cost + 20  # amount of down payment
    balance = laptop_cost - down_payment  # remaining balance
    remaining_months = 4  # number of months for installment payments
    monthly_payment = 65  # installment payment per month

    # Calculate the remaining balance after 4 months of installment payments
    for i in range(remaining_months):
        balance = balance - monthly_payment

    result = balance
    return result

print(solution())