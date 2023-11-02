def solution():
    water_to_evaporate = 400
    pool_capacity = 2000
    percent_full = 80
    jump_capacity = (pool_capacity * percent_full) / 100
    result = jump_capacity / water_to_evaporate
    return result

print(solution())