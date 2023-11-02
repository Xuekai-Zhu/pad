def solution():
    
    red_hats = 6
    blue_boots = 9
    both_red_and_blue = 3
    total_cookies = red_hats + blue_boots - both_red_and_blue
    percentage_red_hats = (red_hats / total_cookies) * 100
    result = percentage_red_hats
    return result

print(solution())