def solution():
    """Candy baked four trays with 24 cookies in each tray. She then divided the cookies equally into eight packs. How many cookies did Candy place in each pack?"""
    # Define the total number of cookies
    total_cookies = 4 * 24

    # Calculate the number of cookies in each pack
    cookies_per_pack = total_cookies / 8

    # Round the result to the nearest whole number
    result = round(cookies_per_pack)
    return result

print(solution())