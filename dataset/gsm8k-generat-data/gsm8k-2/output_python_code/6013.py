def solution():
    """Sean buys 3 cans of soda, 2 soups, and 1 sandwich. Each soup cost as much as the 3 combined sodas. The sandwich cost 3 times as much as the soup. If the soda cost $1 how much did everything cost together?"""
    soda_cost = 1
    soup_cost = 3 * soda_cost
    sandwich_cost = 3 * soup_cost
    total_cost = 3 * soda_cost + 2 * soup_cost + sandwich_cost
    result = total_cost
    return result

print(solution())