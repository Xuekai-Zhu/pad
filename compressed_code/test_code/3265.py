def solution():
    
    total_time = 2 * 60  
    baking_time = 15
    white_icing_time = 30
    chocolate_icing_time = 30
    total_cookie_time = baking_time + white_icing_time + chocolate_icing_time
    num_cookies = total_time // total_cookie_time
    dough_cooling_time = total_time - (num_cookies * total_cookie_time)
    result = dough_cooling_time
    return result

print(solution())