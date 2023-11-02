def solution():
    """The swimming club went to a swim meet in another town. They took 2 cars and 3 vans. There were 5 people in each car and 3 people in each van. Each car can hold a maximum of 6 people and each van can hold a maximum of 8 people. How many more people could have ridden with the swim team?"""
    car_capacity = 6
    van_capacity = 8
    num_cars = 2
    num_vans = 3
    car_people = 5
    van_people = 3
    total_people = (num_cars * car_capacity * car_people) + (num_vans * van_capacity * van_people)
    excess_people = (num_cars * car_capacity * car_people) + (num_vans * van_capacity * van_people) - total_people
    result = excess_people
    return result

print(solution())