def solution():
    """Cindy and Olaf made 15 candied apples which they will be selling for $2 each, and 12 candied grapes which they will be selling for $1.5. How much will they earn if they sell everything?"""
    # Define the price of each item
    APPLE_PRICE = 2
    GRAPE_PRICE = 1.5

    # Define the number of each item
    apple_count = 15
    grape_count = 12

    # Calculate the earnings from selling the apples
    apple_earnings = apple_count * APPLE_PRICE

    # Calculate the earnings from selling the grapes
    grape_earnings = grape_count * GRAPE_PRICE

    # Calculate the total earnings
    total_earnings = apple_earnings + grape_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())