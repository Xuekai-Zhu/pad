def solution():
    # Calculate John's annual profit
    rental_income = 900 * 12  # monthly rent * 12 months
    sublet_income = 400 * 3 * 12  # monthly sublet income * 3 subletters * 12 months
    annual_profit = rental_income - sublet_income
    result = annual_profit
    return result

print(solution())