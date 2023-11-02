def solution():
    car_people = 5  # It takes 5 people to lift a car
    truck_people = 2 * car_people  # It takes twice as many people to lift a truck
    num_cars = 6
    num_trucks = 3

    # Calculate the total number of people needed to lift the cars and trucks
    total_people_needed = (car_people * num_cars) + (truck_people * num_trucks)
    result = total_people_needed
    return result

print(solution())