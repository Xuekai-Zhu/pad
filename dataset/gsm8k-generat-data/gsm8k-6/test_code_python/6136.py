def solution():
    # Calculate the total number of cookies baked by Candy
    total_cookies = 4 * 24  # four trays with 24 cookies in each tray
    
    # Calculate the number of cookies in each pack
    cookies_per_pack = total_cookies / 8  # divide the cookies equally into 8 packs
    
    result = cookies_per_pack
    return result

print(solution())