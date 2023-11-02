def solution():
    allowance_per_week = 10
    num_weeks = 4

    # Calculate the total allowance earned over four weeks
    total_allowance = allowance_per_week * num_weeks

    # Calculate the amount spent on the video game
    video_game_cost = total_allowance / 2

    # Calculate the amount remaining after buying the video game
    remaining_money = total_allowance - video_game_cost

    # Calculate the amount spent on the book
    book_cost = remaining_money / 4

    # Calculate the amount James has left after buying the book
    remaining_money -= book_cost

    result = remaining_money
    return result

print(solution())