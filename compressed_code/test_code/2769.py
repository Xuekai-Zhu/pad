def solution():
    
    initial_water = 6000
    evaporated_water = 2000
    drained_water = 3500
    remaining_water = initial_water - evaporated_water - drained_water

    for i in range(3):
        remaining_water += 350
        

    result = remaining_water
    return result

print(solution())