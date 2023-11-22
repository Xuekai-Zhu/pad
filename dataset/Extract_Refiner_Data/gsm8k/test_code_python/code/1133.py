def solution():
    
    # Define the minimum temperature Donny can only drink in the first two mugs
    MIN_TEMP = 40

    # Define the temperature of the mug
    mug_temp = 33

    # Calculate the total temperature Donny has
    total_temp = mug_temp * 2

    # Calculate the temperature Donny pours from the 33-degree mug into his water bottle
    bottle_temp = 4 * mug_temp

    # Calculate the temperature Donny pours from the other bottle
    other_temp = 1 * mug_temp

    # Calculate the total temperature Donny pours from the other bottle
    bottle_other_temp = other_temp + bottle_temp

    # Calculate the temperature Donny can still drink in the second bottle
    second_bottle_temp = MIN_TEMP + bottle_other_temp - total_temp

    # Display the temperature at least the second bottle
    result = second_bottle_temp
    return result

print(solution())