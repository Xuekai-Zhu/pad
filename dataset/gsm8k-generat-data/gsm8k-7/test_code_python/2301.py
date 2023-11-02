def solution():
    initial_snowflakes = 10
    additional_snowflakes = 4
    target_snowflakes = 58

    # Calculate how many additional sets of snowflakes are needed to reach the target
    sets_needed = (target_snowflakes - initial_snowflakes) / additional_snowflakes

    # Calculate the time it takes to get the additional sets needed
    time_needed = sets_needed * 5

    result = time_needed
    return result

print(solution())