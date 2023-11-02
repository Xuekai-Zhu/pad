def solution():
    # Calculate the total amount of money earned in 4 weeks
    total_money = 10 * 4

    # Calculate the amount of money spent on a video game
    video_game_cost = total_money / 2
    remaining_money = total_money - video_game_cost

    # Calculate the amount of money spent on a book
    book_cost = remaining_money / 4
    remaining_money = remaining_money - book_cost

    result = remaining_money
    return result

print(solution())