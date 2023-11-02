def solution():
    lego_sets_sold = 13  # John has 13 lego sets
    price_per_lego_set = 15  # John sells each lego set for $15
    num_video_games = 8  # John buys 8 video games
    price_per_video_game = 20  # John buys each video game for $20
    remaining_money = 5  # John has $5 left after buying the video games

    # Calculate the total revenue from selling the video games
    total_revenue = (price_per_leg_set * num_video_games) - remaining_money

    # Calculate the number of lego sets John still has
    lego_sets_remaining = total_revenue - lego_sets_sold
    result = lego_sets_remaining
    return result

print(solution())