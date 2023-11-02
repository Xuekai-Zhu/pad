def solution():
    """Laura’s House is a 20-mile round trip from her school. The supermarket is 10 miles farther away from the school. If Laura drives to school every morning and two afternoons a week drives to the supermarket. How many miles does Laura driver per week?"""
    # Define the distances
    house_to_school = 20
    school_to_supermarket = 10
    supermarket_to_school = school_to_supermarket

    # Calculate the total distance Laura drives per day
    daily_distance = (2 * house_to_school) + school_to_supermarket

    # Calculate the total distance Laura drives per week
    weekly_distance = (5 * daily_distance) + (2 * supermarket_to_school)

    result = weekly_distance
    return result

print(solution())