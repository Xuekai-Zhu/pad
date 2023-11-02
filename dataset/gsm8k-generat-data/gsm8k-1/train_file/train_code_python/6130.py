def solution():
    """James is sitting outside, counting how many people go past him in vehicles. He has counted 52 vehicles so far today. He saw 12 trucks, a couple of buses, twice as many taxis, some motorbikes, and 30 cars. If the trucks held 2 people each, the buses held 15 people each, the taxis held 2 people each, the motorbikes held 1 person each, and the cars held 3 people each, how many passengers has James seen today?"""
    total_vehicles = 52
    trucks = 12
    buses = 2
    taxis = buses * 2
    cars = 30
    motorbikes = total_vehicles - (trucks + buses + taxis + cars)
    truck_passengers = trucks * 2
    bus_passengers = buses * 15
    taxi_passengers = taxis * 2
    car_passengers = cars * 3
    motorbike_passengers = motorbikes * 1
    total_passengers = truck_passengers + bus_passengers + taxi_passengers + car_passengers + motorbike_passengers
    result = total_passengers
    return result

print(solution())