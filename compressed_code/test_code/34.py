def solution():
    
    first_earthquake = 4
    second_earthquake = first_earthquake * 2
    third_earthquake = second_earthquake * 2
    fourth_earthquake = third_earthquake * 2
    total_buildings = first_earthquake + second_earthquake + third_earthquake + fourth_earthquake
    result = total_buildings
    return result

print(solution())