def solution():
    # Define the amount of coal required to travel 1 mile
    coal_per_mile = 2 / 5

    # Determine how far the train can travel with the remaining coal
    distance_traveled = coal_per_mile * 160

    result = distance_traveled
    return result

print(solution())