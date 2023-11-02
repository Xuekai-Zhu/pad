def solution():
    """The pirates plan to explore 4 islands. Two islands require walking 20 miles per day while the other two islands require 25 miles per day. How many miles will they have to walk if it takes 1.5 days to explore each island?"""
    islands_walking_20_miles = 2
    islands_walking_25_miles = 2
    days_per_island = 1.5
    miles_walking_20_miles = 20 * days_per_island
    miles_walking_25_miles = 25 * days_per_island
    total_miles = (miles_walking_20_miles * islands_walking_20_miles) + (miles_walking_25_miles * islands_walking_25_miles)
    result = total_miles
    return result

print(solution())