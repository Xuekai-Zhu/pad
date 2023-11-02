def solution():
    """Bill the miner discovers a vein of fool's gold. He successfully sells 8 ounces to a merchant, but when he tries to sell to the sheriff he's arrested, fined $50 and run out of town on a rail. If Bill earned $9 for every ounce of fool's gold he sold, how much money is he left with?"""
    # Define the price per ounce of fool's gold
    PRICE_PER_OUNCE = 9

    # Define the number of ounces sold
    ounces_sold = 8

    # Calculate the total earnings before the fine
    earnings = ounces_sold * PRICE_PER_OUNCE

    # Subtract the fine from the earnings
    earnings -= 50

    # Display Bill's remaining earnings
    result = earnings
    return result

print(solution())