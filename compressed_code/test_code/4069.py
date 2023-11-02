def solution():
    
    lawn_price = 15
    video_game_price = 45
    book_price = 5
    lawns_mowed = 35
    video_games_wanted = 5
    total_lawn_income = lawn_price * lawns_mowed
    total_video_game_cost = video_game_price * video_games_wanted
    total_book_cost = total_lawn_income - total_video_game_cost
    num_books = total_book_cost // book_price
    result = num_books
    return result

print(solution())