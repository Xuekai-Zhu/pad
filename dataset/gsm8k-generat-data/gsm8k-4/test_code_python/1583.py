def solution():
    """James can buy a new computer for $600 and have it last 6 years, or buy 2 used computers for $200 each that each last 3 years. How much money will he save by picking the cheaper option?"""
    # Calculate the cost of buying a new computer and having it last for 6 years
    new_computer_cost = 600
    new_computer_lifetime = 6
    new_total_cost = new_computer_cost

    # Calculate the cost of buying 2 used computers, each lasting for 3 years
    used_computer_cost = 200
    used_computer_lifetime = 3
    used_total_cost = used_computer_cost * 2

    # Determine which option is cheaper in the long run
    if new_total_cost < used_total_cost:
        cheaper_option = "new computer"
        savings = used_total_cost - new_total_cost
    else:
        cheaper_option = "used computers"
        savings = new_total_cost - used_total_cost

    # Return the amount of money that James will save by picking the cheaper option
    result = savings
    return result

print(solution())