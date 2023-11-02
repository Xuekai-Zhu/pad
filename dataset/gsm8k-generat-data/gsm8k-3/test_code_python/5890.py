def solution():
    """Laura’s House is a 20-mile round trip from her school. The supermarket is 10 miles farther away from the school. If Laura drives to school every morning and two afternoons a week drives to the supermarket. How many miles does Laura driver per week?"""
    # Define the distance to Laura's house and the supermarket
    HOUSE_DISTANCE = 20
    SUPERMARKET_DISTANCE = 30

    # Calculate the total distance Laura drives to school each week
    school_distance = HOUSE_DISTANCE * 2 * 5 # twice a day, five days a week

    # Calculate the total distance Laura drives to the supermarket each week
    supermarket_distance = SUPERMARKET_DISTANCE * 2 # twice a week

    # Calculate the total distance Laura drives per week
    total_distance = school_distance + supermarket_distance

    # Display the total distance Laura drives per week
    result = total_distance
    return result

print(solution())