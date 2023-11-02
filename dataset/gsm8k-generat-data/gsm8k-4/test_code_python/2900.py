def solution():
    """James won a money prize at a charity raffle. He donated half of his winnings back to the charity, then spent $2 on a hot dog to celebrate his win. He had $55 left over. How many dollars did he win?"""
    # Define the amount spent on the hot dog
    hotdog_cost = 2

    # Define the amount left after the hot dog and donation to the charity
    leftover = 55

    # Calculate the amount won before the donation and hot dog
    pre_donation_amount = leftover * 2

    # Calculate the total amount won, including the donation and hot dog cost
    total_winnings = pre_donation_amount + hotdog_cost

    result = total_winnings
    return result

print(solution())