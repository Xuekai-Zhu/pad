def solution():
    
    final_plants = 20
    months = 3
    gifted_plants = 4
    remaining_plants = final_plants + gifted_plants
    initial_plants = remaining_plants // (2**months)
    result = initial_plants
    return result

print(solution())