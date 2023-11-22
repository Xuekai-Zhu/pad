def solution():
    
    # Define the number of minutes Michael runs his horse
    horse_minutes = 30 * 60

    # Calculate the number of miles Michael ran his horse
    miles_run = horse_minutes / 0.5

    # Calculate the number of birds Michael eats
    birds_eaten = miles_run * 0.5

    # Calculate the cost of the hay
    hay_cost = birds_eaten * 3

    # Calculate the total cost of the horse
    total_cost = horse_minutes * 32 + hay_cost

    # Calculate the amount of change Michael has after he buys the hay
    change = 6 * 5 - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())