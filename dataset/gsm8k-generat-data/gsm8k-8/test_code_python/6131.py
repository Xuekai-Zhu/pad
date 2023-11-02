def solution():
    # Calculate the number of people in trucks
    truck_people = 12 * 2

    # Calculate the number of people in buses
    bus_people = 2 * 15

    # Calculate the number of people in taxis
    taxi_people = 2 * (2 * truck_people)

    # Calculate the number of people in motorbikes
    motorbike_people = (52 - 12 - 2 - 2 - 30) * 1

    # Calculate the number of people in cars
    car_people = 30 * 3

    # Calculate the total number of people James has seen
    total_people = truck_people + bus_people + taxi_people + motorbike_people + car_people

    result = total_people
    return result

print(solution())