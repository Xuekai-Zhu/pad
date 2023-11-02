def solution():
    """A pound of strawberries costs $2.20 and a pound of cherries costs 6 times as much as strawberries. If Briget will buy 5 pounds of strawberries and 5 pounds of cherries, how much will it cost?"""
    # Define the price of strawberries per pound and the price of cherries relative to strawberries
    STRAWBERRY_PRICE = 2.20
    CHERRY_PRICE_MULTIPLIER = 6

    # Define the amount of strawberries and cherries Briget will buy
    STRAWBERRY_AMT = 5
    CHERRY_AMT = 5

    # Calculate the cost of the strawberries and cherries
    strawberry_cost = STRAWBERRY_AMT * STRAWBERRY_PRICE
    cherry_cost = CHERRY_AMT * STRAWBERRY_PRICE * CHERRY_PRICE_MULTIPLIER

    # Calculate the total cost
    total_cost = strawberry_cost + cherry_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())