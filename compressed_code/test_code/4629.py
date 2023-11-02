def solution():
    
    canvas_c02 = 600
    plastic_c02_per_bag = 4 / 16  
    bags_per_trip = 8
    trips = canvas_c02 / (bags_per_trip * plastic_c02_per_bag)
    result = trips
    return result

print(solution())