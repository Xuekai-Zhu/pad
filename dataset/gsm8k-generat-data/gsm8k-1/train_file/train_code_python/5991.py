def solution():
    """Bill's roof can bear 500 pounds of weight. If 100 leaves fall on his roof every day, and 1000 leaves weighs 1 pound, how many days will it take for his roof to collapse?"""
    weight_capacity = 500
    leaves_per_day = 100
    leaves_per_pound = 1000
    weight_per_day = leaves_per_day / leaves_per_pound
    days_until_collapse = weight_capacity / weight_per_day
    result = days_until_collapse
    return result

print(solution())