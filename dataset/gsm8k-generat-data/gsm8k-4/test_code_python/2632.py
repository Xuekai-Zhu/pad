def solution():
    """The swimming club went to a swim meet in another town. They took 2 cars and 3 vans. There were 5 people in each car and 3 people in each van. Each car can hold a maximum of 6 people and each van can hold a maximum of 8 people.  How many more people could have ridden with the swim team?"""
    # Define the maximum capacity of each car and van
    CAR_CAPACITY = 6
    VAN_CAPACITY = 8

    # Define the number of cars and vans taken by the swim team
    num_cars = 2
    num_vans = 3

    # Calculate the total number of people in the cars and vans
    total_people = (num_cars * 5) + (num_vans * 3)

    # Calculate the maximum number of people that could have ridden with the swim team
    max_capacity = (num_cars * CAR_CAPACITY) + (num_vans * VAN_CAPACITY)

    # Calculate the number of people that could have ridden with the swim team
    potential_capacity = max_capacity - total_people

    # return the result
    result = potential_capacity
    return result

print(solution())