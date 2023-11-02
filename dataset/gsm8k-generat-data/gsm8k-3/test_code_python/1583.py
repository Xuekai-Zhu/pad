def solution():
    """James can buy a new computer for $600 and have it last 6 years, or buy 2 used computers for $200 each that each last 3 years. How much money will he save by picking the cheaper option?"""
    # Calculate the cost of buying a new computer and having it last 6 years
    new_cost = 600
    new_years = 6
    new_yearly_cost = new_cost / new_years

    # Calculate the cost of buying two used computers and having each last 3 years
    used_cost = 2 * 200
    used_years = 3
    used_yearly_cost = used_cost / (2 * used_years)

    # Determine which option is cheaper and calculate the savings
    if new_yearly_cost < used_yearly_cost:
        savings = (used_yearly_cost - new_yearly_cost) * new_years
    else:
        savings = 0

    # Display the savings
    result = savings
    return result

print(solution())