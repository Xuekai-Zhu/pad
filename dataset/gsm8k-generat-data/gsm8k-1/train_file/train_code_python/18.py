def solution():
    """It takes Roque two hours to walk to work and one hour to ride his bike to work. Roque walks to and from work three times a week and rides his bike to and from work twice a week. How many hours in total does he take to get to and from work a week with walking and biking?"""
    walk_time = 2 # hours
    bike_time = 1 # hour
    walk_frequency = 3 # times per week
    bike_frequency = 2 # times per week
    total_walk_time = walk_time * 2 * walk_frequency # walking to and from work
    total_bike_time = bike_time * 2 * bike_frequency # biking to and from work
    total_time = total_walk_time + total_bike_time
    result = total_time
    return result

print(solution())