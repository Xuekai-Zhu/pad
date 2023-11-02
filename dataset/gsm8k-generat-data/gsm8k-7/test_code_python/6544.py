def solution():
    amount_left = 100
    money_spent = 20
    charity_share = 0.5

    # Calculate how much George had before spending on groceries and donating to charity
    total_money = amount_left + money_spent

    # Calculate how much George earned in a month
    monthly_income = total_money / (1 - charity_share)
    result = monthly_income
    return result

print(solution())