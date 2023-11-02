def solution():
    """Tom fills a 250 pound sandbag 80% full. But the filling material he is using is 40% heavier than sand. How much does the bag weigh?"""
    initial_weight = 250
    fill_percentage = 0.8
    fill_weight_ratio = 1.4
    fill_weight = initial_weight * fill_percentage * fill_weight_ratio
    total_weight = initial_weight + fill_weight
    result = total_weight
    return result

print(solution())