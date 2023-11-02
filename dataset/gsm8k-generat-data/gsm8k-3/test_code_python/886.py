def solution():
    """Jack went to a supermarket with $100 and bought 4 bottles of water. Then his mother called him and asked him to buy twice as many bottles as he already bought. Each bottle cost $2, and he also bought half a pound of cheese for $5. How much money does Jack have remaining?"""
    # Define the initial amount of money Jack had
    initial_money = 100

    # Calculate the cost of the bottles of water
    water_cost = 4 * 2

    # Calculate the total number of bottles of water bought
    total_bottles = 4 + (2 * 4)

    # Calculate the cost of the cheese
    cheese_cost = 10 * 0.5

    # Calculate the total cost of everything
    total_cost = water_cost + cheese_cost

    # Calculate the remaining amount of money Jack has
    remaining_money = initial_money - total_cost

    # Display the remaining amount of money Jack has
    result = remaining_money
    return result

print(solution())