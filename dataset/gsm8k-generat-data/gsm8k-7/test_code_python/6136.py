def solution():
    num_trays = 4
    cookies_per_tray = 24
    num_packs = 8

    # Calculate the total number of cookies
    total_cookies = num_trays * cookies_per_tray

    # Calculate the number of cookies in each pack
    cookies_per_pack = total_cookies / num_packs
    result = cookies_per_pack
    return result

print(solution())