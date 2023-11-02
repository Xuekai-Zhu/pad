def solution():
    lawn_price = 15.0
    num_lawns = 35

    video_game_price = 45.0
    num_video_games = 5

    book_price = 5.0

    # Calculate the total income from mowing lawns
    total_income = num_lawns * lawn_price

    # Calculate the total cost of all video-games
    total_video_game_cost = num_video_games * video_game_price

    # Calculate the amount of money left after buying all the video-games
    money_left = total_income - total_video_game_cost

    # Calculate the number of books Kenny can buy
    num_books = int(money_left / book_price)
    result = num_books
    return result

print(solution())