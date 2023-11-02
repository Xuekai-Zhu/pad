def solution():
    """Bryan bought three different bottles of milk. The bottles contain the following volumes of milk: 2 liters, 750 milliliters, 250 milliliters. How many liters of milk did Bryan buy in total?"""
    # Define the volumes of milk in each bottle
    bottle1 = 2000 # 2 liters (converted to milliliters)
    bottle2 = 750  # milliliters
    bottle3 = 250  # milliliters

    # Calculate the total volume of milk in milliliters
    total_milliliters = bottle1 + bottle2 + bottle3

    # Convert the total volume to liters
    total_liters = total_milliliters / 1000

    # Display the total volume of milk in liters
    result = total_liters
    return result

print(solution())