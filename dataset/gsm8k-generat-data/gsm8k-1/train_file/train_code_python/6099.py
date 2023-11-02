def solution():
    """Grandma Olga has 3 daughters and 3 sons. If all her daughters each have 6 sons, and each of her sons has 5 daughters, how many grandchildren does she have in total?"""
    num_daughters = 3
    num_sons = 3
    grandsons_per_daughter = 6
    granddaughters_per_son = 5
    total_grandchildren = (num_daughters * grandsons_per_daughter) + (num_sons * granddaughters_per_son)
    result = total_grandchildren
    return result

print(solution())