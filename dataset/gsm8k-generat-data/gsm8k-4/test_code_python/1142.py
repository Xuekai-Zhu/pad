def solution():
    """Daytona Beach has 26 shark sightings a year. Daytona Beach has 5 more than triple the number of shark sightings as Cape May. How many shark sightings are there in Cape May?"""
    # Let's say the number of shark sightings in Cape May is x
    # According to the problem, the number of shark sightings in Daytona Beach is 5 more than triple the number in Cape May
    # So, the number of shark sightings in Daytona Beach is 5 + 3x

    # The total number of shark sightings is 26, so:
    # x + (5 + 3x) = 26
    # 4x + 5 = 26
    # 4x = 21
    # x = 5.25

    # Since we can't have a fraction of a shark sighting, we can round up to the nearest whole number
    # The number of shark sightings in Cape May is 6

    result = 6
    return result

print(solution())