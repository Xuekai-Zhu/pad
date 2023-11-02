def solution():
    num_trucks = 12
    num_buses = 2
    num_taxis = num_buses * 2
    num_motorbikes = 52 - num_trucks - num_buses - num_taxis - 30
    num_cars = 30

    truck_passengers = num_trucks * 2
    bus_passengers = num_buses * 15
    taxi_passengers = num_taxis * 2
    motorbike_passengers = num_motorbikes * 1
    car_passengers = num_cars * 3

    total_passengers = truck_passengers + bus_passengers + taxi_passengers + motorbike_passengers + car_passengers
    result = total_passengers
    return result

print(solution())