def solution():
    """Candy baked four trays with 24 cookies in each tray. She then divided the cookies equally into eight packs. How many cookies did Candy place in each pack?"""
    # Define the number of trays and cookies per tray
    NUM_TRAYS = 4
    COOKIES_PER_TRAY = 24

    # Calculate the total number of cookies
    total_cookies = NUM_TRAYS * COOKIES_PER_TRAY

    # Calculate the number of cookies in each pack
    cookies_per_pack = total_cookies / 8

    # Display the number of cookies per pack
    result = cookies_per_pack
    return result

print(solution())