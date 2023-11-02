def solution():
    """Joe’s mother gave him $56 to go to the store. Joe bought 7 notebooks and 2 books. Each notebook costs $4 and each book costs $7. How much money does Joe have left?"""
    total_cost = (7 * 4) + (2 * 7)
    money_left = 56 - total_cost
    result = money_left
    return result

print(solution())