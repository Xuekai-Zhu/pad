def solution():
    """A normal lemon tree produces 60 lemons per year. Jim has specially engineered lemon trees that produce 50% more lemons per year. He has a grove that is 50 trees by 30 trees. How many lemons does he produce in 5 years?"""
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