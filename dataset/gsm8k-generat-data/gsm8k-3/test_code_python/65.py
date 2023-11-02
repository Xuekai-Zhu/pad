def solution():
    """Lee mows one lawn and charges $33. Last week he mowed 16 lawns and three customers each gave him a $10 tip. How many dollars did Lee earn mowing lawns last week?"""
    # Define the price per lawn and the number of lawns mowed
    PRICE_PER_LAWN = 33
    NUM_LAWNS = 16

    # Define the tip amount
    TIP_AMOUNT = 10

    # Calculate the total earnings from mowing lawns
    lawn_earnings = PRICE_PER_LAWN * NUM_LAWNS

    # Calculate the total earnings from tips
    tip_earnings = TIP_AMOUNT * 3

    # Calculate the total earnings
    total_earnings = lawn_earnings + tip_earnings

    result = total_earnings
    return result

print(solution())