def solution():
    # Calculate the maximum number of people that could have ridden with the swim team
    max_people_cars = 2 * 6 * 5  # 2 cars, each with 6 seats, each seat occupied by a person
    max_people_vans = 3 * 8 * 3  # 3 vans, each with 8 seats, each seat occupied by a person
    total_max_people = max_people_cars + max_people_vans  # total maximum number of people

    # Calculate the actual number of people that rode with the swim team
    actual_people_cars = 2 * 5  # 2 cars, each with 5 people
    actual_people_vans = 3 * 3  # 3 vans, each with 3 people
    total_actual_people = actual_people_cars + actual_people_vans  # total actual number of people

    # Calculate the difference between the actual and maximum number of people
    difference = total_max_people - total_actual_people
    result = difference
    return result

print(solution())