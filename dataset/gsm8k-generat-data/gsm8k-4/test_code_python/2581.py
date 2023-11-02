def solution():
    """Kenneth has $50 to go to the store. Kenneth bought 2 baguettes and 2 bottles of water. Each baguette cost $2 and each bottle of water cost $1. How much money does Kenneth have left?"""
    # Define the initial amount of money
    initial_money = 50

    # Define the cost of each baguette and bottle of water
    baguette_cost = 2
    water_cost = 1

    # Calculate the total cost of the baguettes and water
    total_cost = (2 * baguette_cost) + (2 * water_cost)

    # Calculate the amount of money remaining
    remaining_money = initial_money - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())