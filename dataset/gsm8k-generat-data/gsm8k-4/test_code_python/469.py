def solution():
    """Jackson wants to impress his girlfriend by filling her hot tub with champagne. The hot tub holds 40 gallons of liquid. Each bottle of champagne holds 1 quart. (There are 4 quarts per gallon). If each bottle of champagne costs $50, but Jackson gets a 20% volume discount, how much does he spend on champagne?"""
    # Define the volume of the hot tub in quarts
    hot_tub_volume = 40 * 4 * 4

    # Calculate the number of bottles of champagne needed to fill the hot tub
    num_bottles = hot_tub_volume / 32

    # Apply the volume discount
    discounted_price = 50 * 0.8

    # Calculate the total cost of the champagne
    total_cost = num_bottles * discounted_price

    # Return the result
    result = total_cost
    return result

print(solution())