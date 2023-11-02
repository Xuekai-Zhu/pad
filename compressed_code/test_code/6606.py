def solution():
    
    total_water = 1200
    first_neighborhood = 150
    second_neighborhood = first_neighborhood * 2
    third_neighborhood = second_neighborhood + 100
    total_used = first_neighborhood + second_neighborhood + third_neighborhood
    barrels_left = total_water - total_used
    result = barrels_left
    return result

print(solution())