def solution():
    # Calculate the total revenue Kenny earns from mowing lawns
    total_revenue = 15 * 35  # Kenny charges $15 per lawn and mows 35 lawns

    # Calculate the cost of the video-games
    video_games_cost = 45 * 5  # Kenny wants to buy 5 video-games at $45 each

    # Calculate the amount of money remaining after buying the video-games
    remaining_money = total_revenue - video_games_cost

    # Calculate the maximum number of books Kenny can buy with the remaining money
    books_qty = remaining_money // 5  # each book costs $5

    result = books_qty
    return result

print(solution())