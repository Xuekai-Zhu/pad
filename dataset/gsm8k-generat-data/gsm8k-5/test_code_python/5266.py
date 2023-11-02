def solution():
    lawns_mowed = 35  # Kenny mowed 35 lawns
    lawn_price = 15  # Kenny charges $15 per lawn
    total_earnings = lawns_mowed * lawn_price  # Kenny's total earnings from mowing lawns
    video_game_price = 45  # The cost of one video game is $45
    desired_video_games = 5  # Kenny wants to buy 5 video games

    # Calculate the total cost of the video games
    total_video_game_cost = video_game_price * desired_video_games

    # Calculate the amount of money Kenny has left for books
    remaining_money = total_earnings - total_video_game_cost

    book_price = 5  # The cost of one book is $5

    # Calculate the number of books Kenny can buy with the remaining money
    num_books = remaining_money // book_price
    result = num_books
    return result

print(solution())