def solution():
    gas_cost = 17  # Tom spends $17 on gas each month
    num_lawns = 3  # Tom mows 3 lawns each month
    lawn_cost = 12  # Tom charges $12 per lawn mowed
    weed_income = 10  # Tom made an extra $10 pulling weeds

    # Calculate total income
    total_income = (num_lawns * lawn_cost) + weed_income

    # Calculate total expenses
    total_expenses = gas_cost

    # Calculate profit
    profit = total_income - total_expenses
    result = profit
    return result

print(solution())