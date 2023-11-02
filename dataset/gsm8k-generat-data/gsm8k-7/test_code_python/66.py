def solution():
    laptop_cost = 1000
    payment_per_month = 65
    down_payment_percent = 0.2
    additional_down_payment = 20
    num_months = 4

    # Calculate the down payment
    down_payment = laptop_cost * down_payment_percent + additional_down_payment

    # Calculate the remaining balance after the down payment
    remaining_balance = laptop_cost - down_payment

    # Calculate the total amount paid after 4 months
    total_paid = down_payment + payment_per_month * num_months

    # Calculate the remaining balance after 4 months of payment
    balance_after_4_months = remaining_balance - payment_per_month * (num_months - 1)

    result = balance_after_4_months
    return result

print(solution())