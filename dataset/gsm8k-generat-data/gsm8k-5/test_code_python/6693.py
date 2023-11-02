def solution():
    growth_per_month = 1.5  # John's hair grows 1.5 inches every month
    length_before_haircut = 9  # John cuts his hair every time it gets to 9 inches
    length_after_haircut = 6  # John cuts his hair down to 6 inches

    # Calculate how many times John gets a haircut in a year
    months_between_haircuts = length_before_haircut / growth_per_month
    haircuts_per_year = 12 / months_between_haircuts

    # Calculate the cost of one haircut, including tip
    haircut_cost = 45 * 1.2  # John gives a 20% tip

    # Calculate the total cost of haircuts in a year
    total_cost = haircuts_per_year * haircut_cost
    result = total_cost
    return result

print(solution())