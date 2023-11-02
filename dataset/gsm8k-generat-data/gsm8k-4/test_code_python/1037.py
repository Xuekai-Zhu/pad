def solution():
    """John buys a gaming PC for $1200. He decides to replace the video card in it. He sells the old card for $300 and buys a new one for $500. How much money did he spend on his computer, counting the savings from selling the old card?"""
    # Define the initial cost of the PC and the cost of the new video card
    initial_cost = 1200
    new_card_cost = 500

    # Define the amount saved by selling the old video card
    saved_amount = 300

    # Calculate the total cost after replacing the video card
    total_cost = initial_cost + new_card_cost - saved_amount

    # Return the result
    result = total_cost
    return result

print(solution())