def solution():
    """Cindy and Olaf made 15 candied apples which they will be selling for $2 each, and 12 candied grapes which they will be selling for $1.5. How much will they earn if they sell everything?"""
    # Define the prices of candied apples and grapes
    apple_price = 2
    grape_price = 1.5

    # Define the number of candied apples and grapes
    num_apples = 15
    num_grapes = 12

    # Calculate the total earnings from selling candied apples and grapes
    apple_earnings = num_apples * apple_price
    grape_earnings = num_grapes * grape_price
    total_earnings = apple_earnings + grape_earnings

    # Return the total earnings
    result = total_earnings
    return result

print(solution())