def solution():
    """Chris wanted to buy a new video game that costs $60 as well as an assortment of candy that costs $5.  To earn the money, he agreed to babysit his little sister for $8 per hour.  If he works 9 hours, how much money will be left over after he makes his purchases?"""
    # Define the cost of the video game and candy
    GAME_COST = 60
    CANDY_COST = 5

    # Calculate Chris's earnings from babysitting
    babysitting_earnings = 8 * 9

    # Calculate the total cost of the video game and candy
    total_cost = GAME_COST + CANDY_COST

    # Calculate the amount of money Chris will have left over
    left_over = babysitting_earnings - total_cost

    # Display the amount of money left over
    result = left_over
    return result

print(solution())