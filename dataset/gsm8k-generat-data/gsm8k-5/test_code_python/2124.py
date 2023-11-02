def solution():
    allowance_per_week = 10  # James earns $10 per week
    weeks = 4  # James saves for 4 weeks
    total_allowance = allowance_per_week * weeks  # Total allowance over the 4 weeks

    # Calculate amount spent on the video game
    video_game_spending = total_allowance / 2

    # Calculate amount remaining after buying the video game
    remaining_money = total_allowance - video_game_spending

    # Calculate amount spent on the book
    book_spending = remaining_money / 4

    # Calculate final amount of money left
    final_money = remaining_money - book_spending
    result = final_money
    return result

print(solution())