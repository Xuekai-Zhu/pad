def solution():
    initial_value = 100  # Ben paid $100 for the lawnmower
    first_depreciation = 0.25  # The mower dropped in value by 25% after 6 months
    second_depreciation = 0.2  # The mower dropped in value by 20% over the next year

    # Calculate the current value of the lawnmower after the first depreciation
    first_value = initial_value - (initial_value * first_depreciation)

    # Calculate the current value of the lawnmower after the second depreciation
    final_value = first_value - (first_value * second_depreciation)

    result = final_value
    return result

print(solution())