def solution():
    num_daughters = 3
    num_sons = 3

    num_grandsons_per_daughter = 6
    num_granddaughters_per_son = 5

    # Calculate the total number of grandsons
    total_grandsons = num_daughters * num_grandsons_per_daughter

    # Calculate the total number of granddaughters
    total_granddaughters = num_sons * num_granddaughters_per_son

    # Calculate the total number of grandchildren
    total_grandchildren = total_grandsons + total_granddaughters
    result = total_grandchildren
    return result

print(solution())