def solution():
    deposit_percent = 0.1  # 10% deposit
    price_last_year = 250
    price_increase_percent = 0.4  # 40% increase

    # Calculate the deposit amount
    deposit_amount = price_last_year * deposit_percent

    # Calculate the total price of this year's costume
    price_this_year = price_last_year * (1 + price_increase_percent)

    # Calculate the amount Jeff pays when picking up the costume
    amount_due = price_this_year - deposit_amount
    result = amount_due
    return result

print(solution())