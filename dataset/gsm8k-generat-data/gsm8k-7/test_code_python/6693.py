def solution():
    growth_rate = 1.5  # inches per month
    haircut_length = 6  # inches
    required_length = 9  # inches
    haircut_cost = 45
    tip_percentage = 0.2
    months_per_year = 12

    # Calculate the number of haircuts John needs per year
    growth_per_year = growth_rate * months_per_year
    num_haircuts = growth_per_year // (required_length - haircut_length)

    # Calculate the total cost of all haircuts John will get
    total_cost = num_haircuts * (haircut_cost * (1 + tip_percentage))
    result = total_cost
    return result

print(solution())