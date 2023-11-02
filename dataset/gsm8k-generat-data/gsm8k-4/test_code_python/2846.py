def solution():
    """Chris wanted to buy a new video game that costs $60 as well as an assortment of candy that costs $5. To earn the money, he agreed to babysit his little sister for $8 per hour. If he works 9 hours, how much money will be left over after he makes his purchases?"""
    # Define the cost of the video game and candy
    game_cost = 60
    candy_cost = 5

    # Calculate the total earnings from babysitting
    earnings = 8 * 9

    # Calculate the total cost of purchases
    total_cost = game_cost + candy_cost

    # Calculate the remaining money after purchases
    remaining_money = earnings - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())