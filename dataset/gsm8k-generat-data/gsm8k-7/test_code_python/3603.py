def solution():
    robi_contribution = 4000
    rudy_contribution = 5/4 * robi_contribution  # Rudy contributed 1/4 more than Robi
    total_contribution = robi_contribution + rudy_contribution

    # Calculate the profit of the business
    profit = 0.2 * total_contribution

    # Calculate the total amount of money that Robi and Rudy each received
    total_amount = total_contribution + profit
    amount_each = total_amount / 2

    result = amount_each
    return result

print(solution())