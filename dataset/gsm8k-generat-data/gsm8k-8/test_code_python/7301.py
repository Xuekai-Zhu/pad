def solution():
    # Define the number of paychecks and contribution amount
    paychecks_per_year = 26
    contribution_per_paycheck = 100.00

    # Calculate the total contribution from Holly and her company
    total_contribution = (contribution_per_paycheck * paychecks_per_year) * (1 + 0.06)

    result = total_contribution
    return result

print(solution())