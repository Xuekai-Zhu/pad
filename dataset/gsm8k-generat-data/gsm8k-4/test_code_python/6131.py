def solution():
    """James is sitting outside, counting how many people go past him in vehicles. He has counted 52 vehicles so far today. He saw 12 trucks, a couple of buses, twice as many taxis, some motorbikes, and 30 cars. If the trucks held 2 people each, the buses held 15 people each, the taxis held 2 people each, the motorbikes held 1 person each, and the cars held 3 people each, how many passengers has James seen today?"""
    # Define the number of vehicles
    total_vehicles = 52

    # Calculate the number of people in the trucks
    truck_passengers = 12 * 2

    # Calculate the number of people in the buses
    bus_passengers = 2 * 15

    # Calculate the number of people in the taxis
    taxi_passengers = 2 * total_vehicles

    # Calculate the number of people in the cars
    car_passengers = 30 * 3

    # Calculate the total number of passengers
    total_passengers = truck_passengers + bus_passengers + taxi_passengers + car_passengers

    # return the result
    result = total_passengers
    return result

print(solution())