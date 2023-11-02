def solution():
    """James earns $10 per week as an allowance. After saving all his money for four weeks, he spends half of it on a new video game. He then spends a quarter of what is left to buy a new book. How much money does he have left?"""
    # Define the amount earned per week and the number of weeks
    WEEKLY_ALLOWANCE = 10
    WEEKS = 4

    # Calculate the total amount saved
    total_saved = WEEKLY_ALLOWANCE * WEEKS

    # Calculate the amount spent on the video game
    video_game_spending = total_saved / 2

    # Calculate the amount remaining after buying the video game
    remaining_amount = total_saved - video_game_spending

    # Calculate the amount spent on the book
    book_spending = remaining_amount / 4

    # Calculate the final amount remaining
    final_amount = remaining_amount - book_spending

    # return the result
    result = final_amount
    return result

print(solution())