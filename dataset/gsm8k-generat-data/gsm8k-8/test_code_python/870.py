def solution():
    # Calculate the total time it takes to make one cake on a typical day
    total_time_per_cake = 1 + 1.5 + 1
    # Calculate the time it takes to bake the cakes on the day when the oven failed
    baking_time_fails = 2 * 1.5
    # Calculate the total time it takes to make one cake on the day when the oven failed
    total_time_per_cake_fails = 1 + baking_time_fails + 1
    # Calculate the total time it took to make all the cakes on the day the oven failed
    total_time_fails = 12 * total_time_per_cake_fails
    result = total_time_fails
    return result

print(solution())