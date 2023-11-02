def solution():
    """Percy wants to save up for a new PlayStation, which costs $500. He gets $200 on his birthday and $150 at Christmas. To make the rest of the money, he's going to sell his old PlayStation games for $7.5 each. How many games does he need to sell to reach his goal?"""
    # Define the total cost of the new PlayStation
    PLAYSTATION_COST = 500

    # Define the amount of money Percy already has
    current_money = 200 + 150

    # Define the cost of each game
    GAME_PRICE = 7.5

    # Calculate how much money Percy needs to save up by selling games
    remaining_money = PLAYSTATION_COST - current_money

    # Calculate how many games Percy needs to sell to make the remaining money
    games_needed = int(remaining_money / GAME_PRICE)

    # Display the number of games Percy needs to sell
    result = games_needed
    return result

print(solution())