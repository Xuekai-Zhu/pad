def solution():
    Johnson_field_size = 1
    neighbor_field_size = 2
    Johnson_corn_yield = 80
    neighbor_corn_yield = Johnson_corn_yield * 2
    total_corn_yield = Johnson_corn_yield + neighbor_corn_yield
    time_period = 6
    total_corn = total_corn_yield * time_period
    result = total_corn
    return result

print(solution())