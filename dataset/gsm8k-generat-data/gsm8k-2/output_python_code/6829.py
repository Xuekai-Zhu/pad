def solution():
    """Anna is making gingerbread cookies. She gives 6 of them red hats, 9 of them blue boots, and 3 of them both red hats and blue boots. What percentage of the gingerbread men have red hats?"""
    red_hats = 6
    blue_boots = 9
    both_red_and_blue = 3
    total_cookies = red_hats + blue_boots - both_red_and_blue
    percentage_red_hats = (red_hats / total_cookies) * 100
    result = percentage_red_hats
    return result

print(solution())