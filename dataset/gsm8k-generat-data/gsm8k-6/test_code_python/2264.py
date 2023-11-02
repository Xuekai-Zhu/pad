def solution():
    # Calculate the number of people living in Roseville city
    roseville_city = 3 * 2000 - 500  # Roseville city has 500 less than thrice as many people as Willowdale city

    # Calculate the number of people living in Sun City
    sun_city = 2 * roseville_city + 1000  # Sun City has 1000 more than twice as many people as Roseville City

    result = sun_city
    return result

print(solution())