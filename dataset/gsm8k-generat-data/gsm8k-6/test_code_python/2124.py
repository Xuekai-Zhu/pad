def solution():
    # Calculate James' total allowance after 4 weeks
    total_allowance = 10 * 4  # James earns $10 per week as an allowance

    # Calculate how much James spends on the video game
    spent_on_game = total_allowance // 2  # James spends half of his money on the new video game

    # Calculate how much James has left after buying the video game
    money_left = total_allowance - spent_on_game

    # Calculate how much James spends on the new book
    spent_on_book = money_left // 4  # James spends a quarter of what is left on the new book

    # Calculate how much money James has left
    money_left = money_left - spent_on_book

    result = money_left
    return result

print(solution())