def solution():
    # Calculate the amount of money Sheila saves in 4 years
    savings_in_four_years = 276 * 12 * 4  # $276 per month, 12 months in a year, for 4 years

    # Add Sheila's current savings and her family's contribution to get the total amount of money in the piggy bank
    total_savings = 3000 + 7000 + savings_in_four_years

    result = total_savings
    return result

print(solution())