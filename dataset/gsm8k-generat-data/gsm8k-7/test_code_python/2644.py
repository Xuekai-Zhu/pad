def solution():
    total_cupcakes = 96
    cupcakes_given = 24
    days = 2

    # Calculate the remaining cupcakes that Carl needs to sell
    remaining_cupcakes = total_cupcakes - cupcakes_given

    # Calculate the number of cupcakes Carl needs to sell per day
    cupcakes_per_day = remaining_cupcakes / days
    result = cupcakes_per_day
    return result

print(solution())