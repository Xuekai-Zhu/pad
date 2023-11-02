def solution():
    """John plans to sell all his toys and use the money to buy video games. He has 13 lego sets and he sells them for $15 each. He ends up buying 8 video games for $20 each and has $5 left. How many lego sets does he still have?"""
    num_lego_sets = 13
    lego_price = 15
    lego_sales = num_lego_sets * lego_price
    video_game_price = 20
    num_video_games = 8
    video_game_cost = num_video_games * video_game_price
    total_money = lego_sales - video_game_cost + 5
    lego_sets_left = total_money // lego_price
    result = num_lego_sets - lego_sets_left
    return result

print(solution())