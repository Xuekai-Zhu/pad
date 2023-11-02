def solution():
    """If Patty's dress was $10 more than Ida's dress, and Ida's dress was $30 more than Jean's dress, and Jean's dress was $10 less than Pauline's dress, and lastly Pauline's dress was $30, how much did all the ladies spend on dressed put together?"""
    pauline_dress_price = 30
    jean_dress_price = pauline_dress_price - 10
    ida_dress_price = jean_dress_price + 30
    patty_dress_price = ida_dress_price + 10
    total_price = pauline_dress_price + jean_dress_price + ida_dress_price + patty_dress_price
    result = total_price
    return result

print(solution())