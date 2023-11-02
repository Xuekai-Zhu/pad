def solution():
    num_cars = 3
    car_capacity = 4

    num_taxis = 6
    taxi_capacity = 6

    num_vans = 2
    van_capacity = 5

    # Calculate the total number of people in the cars
    total_car_people = num_cars * car_capacity

    # Calculate the total number of people in the taxis
    total_taxi_people = num_taxis * taxi_capacity

    # Calculate the total number of people in the vans
    total_van_people = num_vans * van_capacity

    # Calculate the total number of people on the hike
    total_people = total_car_people + total_taxi_people + total_van_people
    result = total_people
    return result

print(solution())