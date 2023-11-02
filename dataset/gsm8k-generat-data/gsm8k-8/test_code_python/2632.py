def solution():
    # Define the number of cars and vans
    num_cars = 2
    num_vans = 3

    # Define the maximum capacity of each car and van
    car_capacity = 6
    van_capacity = 8

    # Calculate the total number of people on the trip
    total_people = (num_cars * car_capacity) + (num_vans * van_capacity)

    # Calculate the number of people who actually went on the trip
    actual_people = (num_cars * 5) + (num_vans * 3)

    # Calculate the number of additional people who could have gone on the trip
    additional_people = total_people - actual_people
    result = additional_people
    return result

print(solution())