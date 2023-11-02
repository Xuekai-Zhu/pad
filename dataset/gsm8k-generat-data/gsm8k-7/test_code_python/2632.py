def solution():
    num_cars = 2
    car_capacity = 6
    num_vans = 3
    van_capacity = 8

    # Calculate the total number of people in the cars
    total_car_people = num_cars * car_capacity

    # Calculate the total number of people in the vans
    total_van_people = num_vans * van_capacity

    # Calculate the total number of people who went to the swim meet
    total_people = total_car_people + total_van_people

    # Calculate the number of people who could have ridden with the swim team
    max_people = (num_cars * car_capacity) + (num_vans * van_capacity)
    extra_people = max_people - total_people
    result = extra_people
    return result

print(solution())