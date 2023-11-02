def solution():
    # Calculate the total number of cupcakes Carl needs to sell
    total_cupcakes = 96 + 24  # Carl gives 24 cupcakes to Bonnie as payment, so he needs to sell a total of 120 cupcakes
    cupcakes_per_day = total_cupcakes / 2  # Carl has 2 days to sell the cupcakes
    result = cupcakes_per_day
    return result

print(solution())