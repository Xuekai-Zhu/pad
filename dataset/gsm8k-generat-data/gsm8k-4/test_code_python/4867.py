def solution():
    """The first store charges $3 for 6 apples while the second store charges $4 for 10 apples. How many cents can you save on each apple from buying $4 for 10 apples than from $3 for 6 apples?"""
    # Calculate the price per apple at the first store
    store1_price = 3/6

    # Calculate the price per apple at the second store
    store2_price = 4/10

    # Calculate the difference in price per apple
    saved_cents = round(((store1_price - store2_price) * 100), 2)

    result = saved_cents
    return result

print(solution())