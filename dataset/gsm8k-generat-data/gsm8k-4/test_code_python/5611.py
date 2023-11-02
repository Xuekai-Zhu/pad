def solution():
    """The outdoor scouts went on a hike to see a waterfall. To get to the hike, the club members took 3 cars, 6 taxis and 2 vans. There were 4 people in each car, 6 people in each taxis and 5 people in each van. How many people went on the hike?"""
    # Define the number of cars, taxis, and vans
    num_cars = 3
    num_taxis = 6
    num_vans = 2

    # Define the number of people in each car, taxi, and van
    car_capacity = 4
    taxi_capacity = 6
    van_capacity = 5

    # Calculate the total number of people
    total_people = (num_cars * car_capacity) + (num_taxis * taxi_capacity) + (num_vans * van_capacity)

    # return the result
    result = total_people
    return result

print(solution())