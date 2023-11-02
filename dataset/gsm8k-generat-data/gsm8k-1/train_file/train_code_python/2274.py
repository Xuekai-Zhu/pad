def solution():
    """Mary bought six apples from the store. From the apples she bought, for each that Mary ate, she planted two trees from the remaining ones. How many apples did Mary eat?"""
    initial_apples = 6
    trees_planted = initial_apples * 2
    apples_eaten = initial_apples - trees_planted
    result = apples_eaten
    return result

print(solution())