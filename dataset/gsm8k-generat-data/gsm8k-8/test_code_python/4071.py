def solution():
    # Define the starting weight
    starting_weight = 70

    # Calculate the weight gain in the first month
    first_month_gain = 20

    # Calculate the new weight after the first month
    weight_after_first_month = starting_weight + first_month_gain

    # Calculate the weight gain in the second month
    second_month_gain = 30

    # Calculate the new weight after the second month
    weight_after_second_month = weight_after_first_month + second_month_gain

    result = weight_after_second_month
    return result

print(solution())