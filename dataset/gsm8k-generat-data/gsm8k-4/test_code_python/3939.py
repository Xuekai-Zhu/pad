def solution():
    """If Patty's dress was $10 more than Ida's dress, and Ida's dress was $30 more than Jean's dress, and Jean's dress was $10 less than Pauline's dress, and lastly Pauline's dress was $30, how much did all the ladies spend on dresses put together?"""
    # Define the price of Pauline's dress
    pauline_price = 30

    # Calculate Jean's dress price
    jean_price = pauline_price - 10

    # Calculate Ida's dress price
    ida_price = jean_price + 30

    # Calculate Patty's dress price
    patty_price = ida_price + 10

    # Calculate the total price of all the dresses
    total_price = pauline_price + jean_price + ida_price + patty_price

    result = total_price
    return result

print(solution())