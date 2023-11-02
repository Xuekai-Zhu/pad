def solution():
    """If Patty's dress was $10 more than Ida's dress, and Ida's dress was $30 more than Jean's dress, and Jean's dress was $10 less than Pauline's dress, and lastly Pauline's dress was $30, how much did all the ladies spend on dressed put together?"""
    pauline = 30
    jean = pauline - 10
    ida = jean + 30
    patty = ida + 10
    total_spent = pauline + jean + ida + patty
    result = total_spent
    return result

print(solution())