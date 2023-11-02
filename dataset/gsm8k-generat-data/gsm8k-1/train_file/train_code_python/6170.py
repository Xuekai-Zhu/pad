def solution():
    """Ted needs to purchase 5 bananas and 10 oranges. If bananas cost $2 each and oranges cost $1.50 each. How much money does Ted need to purchase 5 bananas and 10 oranges?"""
    bananas_needed = 5
    oranges_needed = 10
    banana_cost = 2
    orange_cost = 1.5
    total_banana_cost = bananas_needed * banana_cost
    total_orange_cost = oranges_needed * orange_cost
    total_cost = total_banana_cost + total_orange_cost
    result = total_cost
    return result

print(solution())