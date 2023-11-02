def solution():
    # Calculate the amount of money Rudy contributed
    rudy_contribution = 1.25 * 4000  # Rudy contributed 1/4 more than Robi

    # Calculate the total amount of money they contributed
    total_contribution = rudy_contribution + 4000

    # Calculate the profit earned by the business
    profit = 0.2 * total_contribution

    # Calculate the amount of money each got after sharing the profits equally
    amount_each = (total_contribution + profit) / 2

    result = amount_each
    return result

print(solution())