def solution():
    """It takes a duck 40 days to fly to the south during winter, twice as much time to fly to the north during summer, and 60 days to travel to the East during spring. How many days is the duck flying during these seasons?"""
    # Calculate the number of days the duck flies during winter to the south
    winter_south_days = 40

    # Calculate the number of days the duck flies during summer to the north
    summer_north_days = winter_south_days * 2

    # Calculate the number of days the duck flies during spring to the east
    spring_east_days = 60

    # Calculate the total number of days the duck is flying
    total_days = winter_south_days + summer_north_days + spring_east_days

    # Display the total number of days
    result = total_days
    return result

print(solution())