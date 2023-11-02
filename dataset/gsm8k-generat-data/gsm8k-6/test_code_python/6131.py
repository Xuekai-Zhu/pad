def solution():
    # Calculate the total number of passengers James has seen today
    trucks = 12
    buses = 2  # a "couple" means 2
    taxis = 2 * buses  # twice as many as buses
    motorbikes = 52 - (trucks + buses + taxis + 30)  # calculate the number of motorbikes
    cars = 30
    
    total_passengers = (trucks * 2) + (buses * 15) + (taxis * 2) + (motorbikes * 1) + (cars * 3)
    result = total_passengers
    return result

print(solution())