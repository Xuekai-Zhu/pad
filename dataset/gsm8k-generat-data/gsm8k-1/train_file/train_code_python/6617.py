def solution():
    """On Blacks, Martha goes to the mall to buy clothes on sale. For every 2 jackets she buys, she gets 1 free jacket. For every 3 t-shirts she buys, she gets 1 free t-shirt. Martha decides to buy 4 jackets and 9 t-shirts. How many clothes will she take home?"""
    jackets_bought = 4
    tshirts_bought = 9
    free_jackets = jackets_bought // 2
    free_tshirts = tshirts_bought // 3
    total_jackets = jackets_bought + free_jackets
    total_tshirts = tshirts_bought + free_tshirts
    result = total_jackets + total_tshirts
    return result

print(solution())