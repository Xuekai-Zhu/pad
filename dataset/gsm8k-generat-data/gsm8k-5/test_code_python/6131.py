def solution():
    # Count the number of passengers in trucks
    passengers_trucks = 12 * 2  # Each truck holds 2 people

    # Count the number of passengers in buses
    passengers_buses = 2 * 15  # There were a couple of buses, each holding 15 people

    # Count the number of passengers in taxis
    taxis = 2 * 12  # There were twice as many taxis as buses and each taxi holds 2 people
    passengers_taxis = taxis * 2

    # Count the number of passengers in motorbikes
    motorbikes = 52 - 12 - 2 - taxis - 30  # Deduct the counted vehicles to get the number of motorbikes
    passengers_motorbikes = motorbikes * 1  # Each motorbike holds 1 person

    # Count the number of passengers in cars
    passengers_cars = 30 * 3  # Each car holds 3 people

    # Total number of passengers counted by James
    total_passengers = passengers_trucks + passengers_buses + passengers_taxis + passengers_motorbikes + passengers_cars
    result = total_passengers
    return result

print(solution())