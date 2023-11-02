def solution():
    total_vehicles = 52
    total_people = 0
    num_trucks = 12
    num_buses = 2
    num_taxis = 2 * total_vehicles / num_trucks
    num_motorbikes = total_vehicles / num_buses
    num_cars = 30
    total_people = (num_trucks * 2) + (num_buses * 15) + (num_taxis * 2) + (num_motorbikes * 1) + (num_cars * 3)
    result = total_people
    return result

print(solution())