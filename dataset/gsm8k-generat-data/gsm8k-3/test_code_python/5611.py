def solution():
    """The outdoor scouts went on a hike to see a waterfall. To get to the hike, the club members took 3 cars, 6 taxis and 2 vans. There were 4 people in each car, 6 people in each taxis and 5 people in each van. How many people went on the hike?"""
    # Define the number of people in each type of vehicle
    CAR_CAPACITY = 4
    TAXI_CAPACITY = 6
    VAN_CAPACITY = 5

    # Define the number of each type of vehicle used
    num_cars = 3
    num_taxis = 6
    num_vans = 2

    # Calculate the total number of people who went on the hike
    total_people = (num_cars * CAR_CAPACITY) + (num_taxis * TAXI_CAPACITY) + (num_vans * VAN_CAPACITY)

    # Display the total number of people
    result = total_people
    return result

print(solution())