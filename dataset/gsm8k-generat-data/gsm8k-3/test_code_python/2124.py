def solution():
    """James earns $10 per week as an allowance. After saving all his money for four weeks, he spends half of it on a new video game. He then spends a quarter of what is left to buy a new book. How much money does he have left?"""
    # Calculate the total amount of money James earns in 4 weeks
    total_earnings = 10 * 4

    # Calculate the amount of money James spends on a video game
    video_game_cost = total_earnings / 2

    # Calculate the amount of money James has left after buying a video game
    remaining_money = total_earnings - video_game_cost

    # Calculate the amount of money James spends on a book
    book_cost = remaining_money / 4

    # Calculate the amount of money James has left after buying a book
    final_amount = remaining_money - book_cost

    # Display the final amount of money James has left
    result = final_amount
    return result

print(solution())