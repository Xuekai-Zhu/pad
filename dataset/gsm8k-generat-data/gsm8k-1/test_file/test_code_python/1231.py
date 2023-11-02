def solution():
    """Michael is traveling on the interstate at an average speed of 50km/hr (taking into account all the necessary stops for gas, relaxation, etc.). If he goes on like this for 3 days, and the distance between Alaska and Texas is 6000 km, what percentage of this distance has he covered?"""
    average_speed = 50
    days_of_travel = 3
    total_distance = 6000
    total_travel_time = 24 * days_of_travel
    distance_covered = total_travel_time * average_speed
    percentage_covered = (distance_covered / total_distance) * 100
    result = percentage_covered
    return result

print(solution())