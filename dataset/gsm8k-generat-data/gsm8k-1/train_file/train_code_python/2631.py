def solution():
    """The swimming club went to a swim meet in another town. They took 2 cars and 3 vans. There were 5 people in each car and 3 people in each van. Each car can hold a maximum of 6 people and each van can hold a maximum of 8 people. How many more people could have ridden with the swim team?"""
    cars = 2
    car_capacity = 6
    vans = 3
    van_capacity = 8
    car_passengers = 5
    van_passengers = 3
    total_passengers = cars * car_passengers + vans * van_passengers
    max_capacity = cars * car_capacity + vans * van_capacity
    remaining_capacity = max_capacity - total_passengers
    result = remaining_capacity
    return result

print(solution())