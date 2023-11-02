def solution():
    """Marcus is having a water balloon party. He has 100 balloons. Each balloon holds 3 ounces of water. He can buy 50 ounces of water for $2.5 a bottle. If he walks into the store with 2 $10 bills, how much change will he have after he buys all the water he needs?"""
    # Define the number of balloons and the amount of water needed in ounces
    num_balloons = 100
    water_needed = num_balloons * 3

    # Define the price of a bottle of water
    water_price = 2.5
    water_per_bottle = 50

    # Calculate the number of bottles of water needed
    num_bottles = water_needed // water_per_bottle + (water_needed % water_per_bottle > 0)

    # Calculate the total cost of the water
    total_cost = num_bottles * water_price

    # Calculate the change after paying with two $10 bills
    change = 20 - total_cost

    result = change
    return result

print(solution())