def solution():
    # Calculate the total money earned from mowing lawns
    total_money = 35 * 15

    # Calculate the cost of the 5 video-games
    game_cost = 5 * 45

    # Subtract the cost of the video-games from the total money
    remaining_money = total_money - game_cost

    # Calculate the number of books he can buy with the remaining money
    book_cost = 5
    num_books = remaining_money // book_cost

    result = num_books
    return result

print(solution())