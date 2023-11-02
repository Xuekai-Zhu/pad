def solution():
    """Lola and Dora combined their allowance of $9 each to buy a deck of playing cards for $10, they also bought $2 boxes of stickers and split the boxes evenly. How many packs of stickers did Dora get?"""
    # Define the total amount of money that Lola and Dora have
    total_money = 9 * 2

    # Define the cost of the deck of playing cards
    deck_cost = 10

    # Define the cost of each box of stickers
    sticker_cost = 2

    # Calculate the amount of money left after buying the deck of playing cards
    remaining_money = total_money - deck_cost

    # Calculate the number of boxes of stickers that can be bought with the remaining money
    num_boxes = remaining_money // sticker_cost

    # Calculate the number of boxes of stickers that Dora gets
    num_dora_boxes = num_boxes // 2  # Divide by 2 since they split the boxes evenly

    # Display the number of packs of stickers that Dora gets
    result = num_dora_boxes
    return result

print(solution())