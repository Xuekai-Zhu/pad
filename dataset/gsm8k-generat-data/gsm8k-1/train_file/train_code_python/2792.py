def solution():
    """Lara is baking cookies using four baking trays. She places five rows of cookies on a baking tray where there are six cookies in one row. How many cookies is she baking?"""
    baking_trays = 4
    rows_per_tray = 5
    cookies_per_row = 6
    total_cookies = baking_trays * rows_per_tray * cookies_per_row
    result = total_cookies
    return result

print(solution())