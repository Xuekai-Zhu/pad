def solution():
    """The outdoor scouts went on a hike to see a waterfall. To get to the hike, the club members took 3 cars, 6 taxis and 2 vans. There were 4 people in each car, 6 people in each taxis and 5 people in each van. How many people went on the hike?"""
    cars = 3
    taxis = 6
    vans = 2
    car_capacity = 4
    taxi_capacity = 6
    van_capacity = 5
    total_people = (cars * car_capacity) + (taxis * taxi_capacity) + (vans * van_capacity)
    result = total_people
    return result

print(solution())