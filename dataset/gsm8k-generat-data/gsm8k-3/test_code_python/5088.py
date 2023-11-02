def solution():
    """Barbara went shopping in a supermarket. She bought 5 packs of tuna for $2 each and 4 bottles of water for $1.5 each.
    In total, she paid $56 for her shopping. How much did Barbara spend on different than the mentioned goods?"""
    # Define the cost of tuna and bottles of water
    TUNA_PRICE = 2
    WATER_PRICE = 1.5

    # Define the number of packs of tuna and bottles of water purchased
    tuna_packs = 5
    water_bottles = 4

    # Calculate the total cost of the tuna
    tuna_cost = tuna_packs * TUNA_PRICE

    # Calculate the total cost of the bottles of water
    water_cost = water_bottles * WATER_PRICE

    # Calculate the total cost of all the purchased goods
    total_cost = tuna_cost + water_cost

    # Calculate how much money was spent on other goods
    other_goods_cost = 56 - total_cost

    # Display how much money was spent on other goods
    result = other_goods_cost
    return result

print(solution())