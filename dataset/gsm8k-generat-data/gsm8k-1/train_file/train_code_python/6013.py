def solution():
    """Sean buys 3 cans of soda, 2 soups, and 1 sandwich. Each soup cost as much as the 3 combined sodas. The sandwich cost 3 times as much as the soup. If the soda cost $1 how much did everything cost together?"""
    soda_price = 1
    soup_price = soda_price * 3
    sandwich_price = soup_price * 3
    total_cost = (3 * soda_price) + (2 * soup_price) + sandwich_price
    result = total_cost
    return result

print(solution())