def solution():
    """Andy and Dawn spent the weekend cleaning the house. When putting away the laundry Andy took six minutes more than two times the number of minutes it took Dawn to wash the dishes. If it took Dawn 20 minutes to wash the dishes how many minutes did it take Andy to put away the laundry?"""
    # Define the time it took Dawn to wash the dishes and the time it took Andy to put away the laundry
    dishes_time = 20
    laundry_time = None

    # Calculate the time it took Andy to put away the laundry
    laundry_time = 2 * dishes_time + 6

    result = laundry_time
    return result

print(solution())