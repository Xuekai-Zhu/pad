def solution():
    """Nina wants to buy a new video game with her allowance money. The game cost 50 dollars. Nina also has learned that there is a 10 percent sales tax. She receives 10 dollars a week as an allowance, and thinks she can save half of that. How many weeks will it take for Nina to be able to buy the new video game with her savings?"""
    # Define the cost of the video game and the sales tax percentage
    game_cost = 50
    sales_tax = 0.1

    # Calculate the total cost of the game including sales tax
    total_cost = game_cost * (1 + sales_tax)

    # Define the amount Nina saves each week
    saving_per_week = 5

    # Initialize the number of weeks it will take to save enough money
    weeks = 0

    # Keep adding to the savings until they are enough to buy the game
    while saving_per_week * weeks < total_cost:
        weeks += 1

    # Return the number of weeks it will take to save enough money
    result = weeks
    return result

print(solution())