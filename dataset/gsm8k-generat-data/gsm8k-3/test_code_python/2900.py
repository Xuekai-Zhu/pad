def solution():
    """James won a money prize at a charity raffle. He donated half of his winnings back to the charity, then spent $2 on a hot dog to celebrate his win. He had $55 left over. How many dollars did he win?"""
    # Define the amount spent on the hot dog
    HOTDOG_PRICE = 2

    # Define the amount left after buying the hot dog
    remaining = 55

    # Calculate the amount James donated back to the charity
    donated = remaining / 2

    # Calculate the total winnings before donating and spending on the hot dog
    total_winnings = remaining + donated + HOTDOG_PRICE

    # Display the total winnings
    result = total_winnings
    return result

print(solution())