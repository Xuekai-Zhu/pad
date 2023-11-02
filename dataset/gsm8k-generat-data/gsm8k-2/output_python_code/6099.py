def solution():
    """Grandma Olga has 3 daughters and 3 sons. If all her daughters each have 6 sons, and each of her sons has 5 daughters, how many grandchildren does she have in total?"""
    num_daughters = 3
    num_sons = 3
    num_granddaughters_per_son = 5
    num_grandsons_per_daughter = 6

    total_grandchildren = num_daughters * num_grandsons_per_daughter * num_sons + num_sons * num_granddaughters_per_son * num_daughters
    result = total_grandchildren
    return result

print(solution())