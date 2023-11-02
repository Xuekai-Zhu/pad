def solution():
    # Define the time it takes to mix, bake, and decorate one cake in minutes
    mix_time = 12
    bake_time = mix_time + 9
    decorate_time = bake_time + 6

    # Calculate the total time to make one cake
    one_cake_time = mix_time + bake_time + decorate_time

    # Calculate the total time to make six cakes in minutes
    total_time = one_cake_time * 6

    # Convert the total time to hours and round to two decimal places
    hours = round(total_time / 60, 2)
    result = hours
    return result

print(solution())