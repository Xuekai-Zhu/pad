def solution():
    
    # Define the time it takes to heat up to 300 degrees
    heat_time_300 = 20

    # Define the time it takes to heat up to 400 degrees, which is 40% longer than the desired temperature
    heat_time_400 = heat_time_300 * 1.4

    # Define the time it takes to warm up the oil
    warm_time_300 = 300 - 5

    # Calculate the total time it takes to cook the oil
    cook_time = heat_time_300 + heat_time_400 - warm_time_300

    # Calculate the time passed from starting the oil to having cooked chicken
    time_passed = cook_time - heat_time_300

    # Display the time passed
    result = time_passed
    return result

print(solution())