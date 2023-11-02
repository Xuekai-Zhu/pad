def solution():
    
    normal_yield = 60
    engineered_yield = normal_yield * 1.5
    grove_width = 50
    grove_length = 30
    total_trees = grove_width * grove_length
    yield_per_tree = engineered_yield
    total_yield = total_trees * yield_per_tree * 5
    result = total_yield
    return result

print(solution())