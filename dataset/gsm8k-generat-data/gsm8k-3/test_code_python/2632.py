def solution():
    """The swimming club went to a swim meet in another town. They took 2 cars and 3 vans. There were 5 people in each car and 3 people in each van. Each car can hold a maximum of 6 people and each van can hold a maximum of 8 people.  How many more people could have ridden with the swim team?"""
    # Define the number of cars and vans
    NUM_CARS = 2
    NUM_VANS = 3

    # Define the maximum capacity for each car and van
    CAR_CAPACITY = 6
    VAN_CAPACITY = 8

    # Calculate the number of people that went to the swim meet
    total_people = NUM_CARS * CAR_CAPACITY + NUM_VANS * VAN_CAPACITY

    # Calculate the number of people that could still ride with the swim team
    remaining_capacity = (NUM_CARS * CAR_CAPACITY + NUM_VANS * VAN_CAPACITY) - (NUM_CARS * 5 + NUM_VANS * 3)

    # Display the remaining capacity
    result = remaining_capacity
    return result

print(solution())