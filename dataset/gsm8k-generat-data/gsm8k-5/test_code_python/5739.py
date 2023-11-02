def solution():
    dress_cost = 80  # The dress costs $80
    savings = 20  # Vanessa has $20 in savings
    weekly_allowance = 30  # Vanessa's parents give her $30 every week
    weekly_expenses = 10  # Vanessa spends $10 every weekend at the arcades

    # Calculate the total amount of money Vanessa can save each week
    weekly_savings = weekly_allowance - weekly_expenses

    # Calculate the total amount of money Vanessa needs to save to buy the dress
    total_savings_needed = dress_cost - savings

    # Calculate the number of weeks Vanessa will have to wait to save enough money
    weeks_to_save = total_savings_needed / weekly_savings
    result = weeks_to_save
    return result

print(solution())