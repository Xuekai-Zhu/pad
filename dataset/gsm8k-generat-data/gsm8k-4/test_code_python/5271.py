def solution():
    """It takes a duck 40 days to fly to the south during winter, twice as much time to fly to the north during summer, and 60 days to travel to the East during spring. How many days is the duck flying during these seasons?"""
    # Define the time it takes the duck to fly to the south
    south_time = 40

    # Define the time it takes the duck to fly to the north
    north_time = south_time * 2

    # Define the time it takes the duck to fly to the east
    east_time = 60

    # Calculate the total time the duck is flying during these seasons
    total_time = south_time + north_time + east_time

    # return the result
    result = total_time
    return result

print(solution())