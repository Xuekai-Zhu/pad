def solution():
    initial_crayons = 18
    lost_crayons = initial_crayons / 2
    new_crayons = 20
    total_crayons = initial_crayons - lost_crayons + new_crayons
    result = total_crayons
    return result

print(solution())