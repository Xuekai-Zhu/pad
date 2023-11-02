def solution():
    # Convert 3 liters to milliliters
    total_water_ml = 3 * 1000

    # Calculate the number of times Sandy drinks 500 ml of water in a day
    num_drinks = total_water_ml // 500

    # Calculate the total time it takes for Sandy to drink 3 liters of water in a day
    total_time = (num_drinks - 1) * 2 + 2  # Sandy drinks every 2 hours, except for the last drink

    result = total_time
    return result

print(solution())