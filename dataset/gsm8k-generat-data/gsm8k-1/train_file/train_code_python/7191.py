def solution():
    """Bobby can deadlift 300 pounds at 13. When he is 18 he can deadlift 100 pounds more than 250% of his previous deadlift. How many pounds did he add per year?"""
    starting_weight = 300
    ending_weight = (starting_weight * 2.5) + 100
    time_span = 18 - 13
    weight_added = (ending_weight - starting_weight) / time_span
    result = weight_added
    return result

print(solution())