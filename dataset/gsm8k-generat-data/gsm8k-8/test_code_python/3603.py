def solution():
    # Calculate Rudy's contribution
    rudy_contribution = 1.25 * 4000

    # Calculate the total amount of money contributed
    total_contribution = rudy_contribution + 4000

    # Calculate the profit earned
    profit = 0.2 * total_contribution

    # Calculate the total amount of money after the profit
    total_amount = total_contribution + profit

    # Calculate the amount each person gets after dividing the total amount equally
    amount_per_person = total_amount / 2
    result = amount_per_person
    return result

print(solution())