def solution():
    """On Blacks, Martha goes to the mall to buy clothes on sale. For every 2 jackets she buys, she gets 1 free jacket. For every 3 t-shirts she buys, she gets 1 free t-shirt. Martha decides to buy 4 jackets and 9 t-shirts. How many clothes will she take home?"""
    # Define the ratio of jackets to free jackets and t-shirts to free t-shirts
    JACKET_RATIO = 2
    FREE_JACKET_RATIO = 1
    TSHIRT_RATIO = 3
    FREE_TSHIRT_RATIO = 1

    # Define the number of jackets and t-shirts purchased
    jackets = 4
    tshirts = 9

    # Calculate the number of free jackets and t-shirts
    free_jackets = jackets // JACKET_RATIO * FREE_JACKET_RATIO
    free_tshirts = tshirts // TSHIRT_RATIO * FREE_TSHIRT_RATIO

    # Calculate the total number of clothes Martha will take home
    total_clothes = jackets + tshirts + free_jackets + free_tshirts

    # Display the total number of clothes
    result = total_clothes
    return result

print(solution())