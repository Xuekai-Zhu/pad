def solution():
    # Calculate John's former rent per month
    former_rent = 2 * 750

    # Calculate John's monthly split of the new rent
    new_rent_split = 2800 / 2

    # Calculate John's monthly savings
    monthly_savings = former_rent - new_rent_split

    # Calculate John's yearly savings
    yearly_savings = monthly_savings * 12

    result = yearly_savings
    return result

print(solution())