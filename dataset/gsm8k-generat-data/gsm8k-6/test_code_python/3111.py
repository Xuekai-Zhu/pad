def solution():
    # Calculate John's former monthly rent, and convert it to yearly rent
    former_rent_monthly = 2 * 750
    former_rent_yearly = former_rent_monthly * 12

    # Calculate John's new monthly rent and the savings he gets
    new_rent_monthly = 2800 / 2
    savings_monthly = former_rent_monthly - new_rent_monthly

    # Convert monthly savings to yearly savings
    savings_yearly = savings_monthly * 12
    result = savings_yearly
    return result

print(solution())