def solution():
    """Roberto is raising chickens for eggs. He buys 4 chickens for $20 each. They cost $1 in total a week to feed and each produces 3 eggs a week that will last forever. He used to buy 1 dozen eggs a week and spent $2 per dozen. After how many weeks will the chickens be cheaper than buying his eggs?"""
    # Define the cost of buying and maintaining the chickens
    CHICKENS_COST = 20 * 4
    CHICKENS_FEED_COST = 1

    # Define the cost of buying eggs
    EGGS_COST = 2

    # Define the number of eggs produced by each chicken per week
    EGGS_PER_CHICKEN_PER_WEEK = 3

    # Define the number of eggs Roberto needs per week
    EGGS_NEEDED_PER_WEEK = 12

    # Initialize the week counter and the total cost of buying eggs
    weeks = 0
    total_eggs_cost = 0

    # Calculate the total cost of buying eggs each week, until the cost of buying and maintaining chickens is less than the cost of buying eggs
    while CHICKENS_COST + (CHICKENS_FEED_COST * weeks) > total_eggs_cost:
        # Increment the week counter
        weeks += 1

        # Calculate the cost of buying eggs for the week
        total_eggs_cost += EGGS_COST

    # Display the number of weeks it took for the chickens to be cheaper than buying eggs
    result = weeks
    return result

print(solution())