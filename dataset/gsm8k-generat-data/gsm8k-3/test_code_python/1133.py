def solution():
    """Marcus is having a water balloon party. He has 100 balloons. Each balloon holds 3 ounces of water. He can buy 50 ounces of water for $2.5 a bottle. If he walks into the store with 2 $10 bills, how much change will he have after he buys all the water he needs?"""
    # Define the number of balloons
    BALLOONS = 100

    # Define the amount of water needed in ounces
    WATER = BALLOONS * 3

    # Define the amount of water in each bottle
    WATER_PER_BOTTLE = 50

    # Define the cost of one bottle of water
    BOTTLE_COST = 2.5

    # Calculate the number of bottles of water needed
    bottles_needed = WATER / WATER_PER_BOTTLE
    # Round up to avoid buying insufficient water
    bottles_needed = math.ceil(bottles_needed)

    # Calculate the cost of all the bottles of water
    total_cost = bottles_needed * BOTTLE_COST

    # Calculate the total amount of money Marcus has
    total_money = 2 * 10

    # Calculate the change Marcus will receive
    change = total_money - total_cost

    result = change
    return result

print(solution())