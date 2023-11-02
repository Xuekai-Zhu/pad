def solution():
    goal_cupcakes = 96  # Carl's goal is to sell 96 cupcakes in 2 days
    cupcakes_given = 24  # Carl needs to give 24 cupcakes to Bonnie as payment
    cupcakes_to_sell = goal_cupcakes - cupcakes_given  # Carl needs to sell this many cupcakes to reach his goal
    days_to_sell = 2  # Carl has 2 days to sell the cupcakes

    # Calculate the number of cupcakes Carl must sell per day to reach his goal
    cupcakes_per_day = cupcakes_to_sell / days_to_sell
    result = cupcakes_per_day
    return result

print(solution())