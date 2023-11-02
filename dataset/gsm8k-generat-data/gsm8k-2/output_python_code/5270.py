def solution():
    """It takes a duck 40 days to fly to the south during winter, twice as much time to fly to the north during summer, and 60 days to travel to the East during spring. How many days is the duck flying during these seasons?"""
    winter_days = 40
    summer_days = winter_days * 2
    spring_days = 60
    total_days = winter_days + summer_days + spring_days
    result = total_days
    return result

print(solution())