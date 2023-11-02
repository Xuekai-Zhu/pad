def solution():
    """It takes Roque two hours to walk to work and one hour to ride his bike to work. Roque walks to and from work three times a week and rides his bike to and from work twice a week. How many hours in total does he take to get to and from work a week with walking and biking?"""
    walk_time = 2
    bike_time = 1
    num_walks = 3
    num_bikes = 2
    total_walk_time = walk_time * 2 * num_walks
    total_bike_time = bike_time * 2 * num_bikes
    total_time = total_walk_time + total_bike_time
    result = total_time
    return result

print(solution())