def solution():
    num_basil_plants = 5
    num_oregano_plants = 2 + 2*num_basil_plants
    total_plants = num_basil_plants + num_oregano_plants
    result = total_plants
    return result

print(solution())