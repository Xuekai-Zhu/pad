def solution():
    """Percy wants to save up for a new PlayStation, which costs $500. He gets $200 on his birthday and $150 at Christmas. To make the rest of the money, he's going to sell his old PlayStation games for $7.5 each. How many games does he need to sell to reach his goal?"""
    # Define the total cost of the PlayStation and the amount of money Percy has already saved
    total_cost = 500
    saved_money = 200 + 150

    # Define the price of each PlayStation game and calculate how many games Percy needs to sell
    game_price = 7.5
    games_needed = (total_cost - saved_money) / game_price

    # Round up to the nearest integer
    games_needed = int(games_needed) + 1

    result = games_needed
    return result

print(solution())