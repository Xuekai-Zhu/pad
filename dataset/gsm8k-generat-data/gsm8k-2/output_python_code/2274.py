def solution():
    """Mary bought six apples from the store. From the apples she bought, for each that Mary ate, she planted two trees from the remaining ones. How many apples did Mary eat?"""
    total_apples = 6
    apples_planted = 2 * (total_apples - 1)
    apples_eaten = total_apples - apples_planted
    result = apples_eaten
    return result

print(solution())