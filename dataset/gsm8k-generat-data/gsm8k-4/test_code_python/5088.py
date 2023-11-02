def solution():
    """Barbara went shopping in a supermarket. She bought 5 packs of tuna for $2 each and 4 bottles of water for $1.5 each. In total, she paid $56 for her shopping. How much did Barbara spend on different than the mentioned goods?"""
    # Define the prices and quantities of the goods
    tuna_price = 2
    tuna_quantity = 5
    water_price = 1.5
    water_quantity = 4

    # Calculate the total cost of the tuna and water
    total_cost = (tuna_price * tuna_quantity) + (water_price * water_quantity)

    # Calculate the amount spent on goods other than tuna and water
    difference = 56 - total_cost

    # Return the result
    result = difference
    return result

print(solution())