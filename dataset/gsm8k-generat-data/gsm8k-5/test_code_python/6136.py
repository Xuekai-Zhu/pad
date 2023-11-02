def solution():
    trays = 4  # Candy baked four trays of cookies
    cookies_per_tray = 24  # Each tray has 24 cookies
    total_cookies = trays * cookies_per_tray  # Total number of cookies baked

    packs = 8  # Candy divided the cookies into 8 packs
    cookies_per_pack = total_cookies / packs  # Divide the cookies equally into 8 packs

    result = cookies_per_pack
    return result

print(solution())