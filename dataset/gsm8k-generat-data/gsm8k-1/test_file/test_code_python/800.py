def solution():
    """Two cars are driving on a highway. The first car is traveling at an average speed of 60 miles per hour when the second car passes it at an average speed of 70 miles per hour. If both cars continue on the highway at the same speed, how many miles will separate them after 2 hours?"""
    speed_car1 = 60
    speed_car2 = 70
    time = 2
    distance_car1 = speed_car1 * time
    distance_car2 = speed_car2 * time
    distance_between_cars = distance_car2 - distance_car1
    result = distance_between_cars
    return result

print(solution())