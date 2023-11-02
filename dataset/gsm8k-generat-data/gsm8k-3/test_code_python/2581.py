def solution():
    """Kenneth has $50 to go to the store. Kenneth bought 2 baguettes and 2 bottles of water. Each baguette cost $2 and each bottle of water cost $1. How much money does Kenneth have left?"""
    # Define the cost of each item
    BAGUETTE_PRICE = 2
    WATER_PRICE = 1

    # Define the number of each item purchased
    baguettes = 2
    waters = 2

    # Calculate the total cost of the items purchased
    total_cost = (baguettes * BAGUETTE_PRICE) + (waters * WATER_PRICE)

    # Calculate the remaining amount of money
    remaining_money = 50 - total_cost

    # Display the remaining amount of money
    result = remaining_money
    return result

print(solution())