def solution():
    # Define the total cupcakes Carl needs to sell
    total_cupcakes = 96

    # Define the number of cupcakes Carl needs to give to Bonnie
    cupcakes_for_bonnie = 24

    # Calculate the remaining cupcakes Carl needs to sell
    cupcakes_left = total_cupcakes - cupcakes_for_bonnie

    # Calculate the number of cupcakes Carl needs to sell each day
    cupcakes_per_day = cupcakes_left / 2
    result = cupcakes_per_day
    return result

print(solution())