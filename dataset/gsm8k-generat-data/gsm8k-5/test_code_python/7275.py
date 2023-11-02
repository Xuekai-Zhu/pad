def solution():
    total_money = 20  # John gives the store $20
    cost_per_slurpee = 2  # Slurpees cost $2 each
    change = 8  # John receives $8 in change

    # Calculate the amount of money spent on Slurpees
    money_spent = total_money - change

    # Calculate the number of Slurpees John bought
    slurpees_bought = money_spent // cost_per_slurpee
    result = slurpees_bought
    return result

print(solution())