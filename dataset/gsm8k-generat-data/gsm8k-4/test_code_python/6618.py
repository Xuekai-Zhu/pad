def solution():
    """On Blacks, Martha goes to the mall to buy clothes on sale. For every 2 jackets she buys, she gets 1 free jacket.
    For every 3 t-shirts she buys, she gets 1 free t-shirt. Martha decides to buy 4 jackets and 9 t-shirts.
    How many clothes will she take home?"""
    # Calculate the number of free jackets Martha will get
    free_jackets = 4 // 2

    # Calculate the number of free t-shirts Martha will get
    free_tshirts = 9 // 3

    # Calculate the total number of jackets Martha will take home
    total_jackets = 4 + free_jackets

    # Calculate the total number of t-shirts Martha will take home
    total_tshirts = 9 + free_tshirts

    # Calculate the total number of clothes Martha will take home
    total_clothes = total_jackets + total_tshirts

    result = total_clothes
    return result

print(solution())