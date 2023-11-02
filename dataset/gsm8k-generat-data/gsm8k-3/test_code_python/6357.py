def solution():
    """Nina wants to buy a new video game with her allowance money. The game cost 50 dollars. Nina also has learned that there is a 10 percent sales tax. She receives 10 dollars a week as an allowance, and thinks she can save half of that. How many weeks will it take for Nina to be able to buy the new video game with her savings?"""
    # Define the cost of the video game and the sales tax rate
    GAME_COST = 50
    SALES_TAX_RATE = 0.1

    # Define Nina's allowance and the portion she can save
    ALLOWANCE = 10
    SAVINGS_RATE = 0.5

    # Calculate the total cost of the game after taxes
    game_cost_with_tax = GAME_COST * (1 + SALES_TAX_RATE)

    # Calculate Nina's savings per week
    savings_per_week = ALLOWANCE * SAVINGS_RATE

    # Calculate the number of weeks it will take for Nina to save enough for the game
    weeks_needed = game_cost_with_tax / savings_per_week

    # Round the number of weeks up to the nearest whole number
    weeks_needed = math.ceil(weeks_needed)

    # Display the number of weeks needed
    result = weeks_needed
    return result

print(solution())