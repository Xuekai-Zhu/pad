def solution():
    """Candy baked four trays with 24 cookies in each tray. She then divided the cookies equally into eight packs. How many cookies did Candy place in each pack?"""
    total_cookies = 4 * 24
    packs = 8
    cookies_per_pack = total_cookies // packs
    result = cookies_per_pack
    return result

print(solution())