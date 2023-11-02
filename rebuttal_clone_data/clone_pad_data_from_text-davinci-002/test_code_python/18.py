def solution():
    """It takes Roque two hours to walk to work and one hour to ride his bike to work. Roque walks to and from work three times a week and rides his bike to and from work twice a week. How many hours in total does he take to get to and from work a week with walking and biking?"""
    walk_time = 2
    bike_time = 1
    walk_trips = 3
    bike_trips = 2
    total_walk_time = walk_time * walk_trips
    total_bike_time = bike_time * bike_trips
    total_time = total_walk_time + total_bike_time
    result = total_time
    
    return result

print(solution())