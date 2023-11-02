def solution():
    
    trucks = 12
    buses = 2
    taxis = 2 * buses
    motorbikes = 52 - (trucks + buses + taxis + 30)
    cars = 30

    total_passengers = (trucks * 2) + (buses * 15) + (taxis * 2) + (motorbikes * 1) + (cars * 3)
    result = total_passengers
    return result

print(solution())