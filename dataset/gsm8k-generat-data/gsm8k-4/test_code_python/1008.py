def solution():
    """Lana aims to sell 20 muffins at the bake sale. She sells 12 muffins in the morning. She sells another 4 in the afternoon. How many more muffins does Lana need to sell to hit her goal?"""
    # Define the target number of muffins to sell
    target_muffins = 20

    # Define the number of muffins sold in the morning and afternoon
    morning_sales = 12
    afternoon_sales = 4

    # Calculate the total number of muffins sold so far
    total_sales = morning_sales + afternoon_sales

    # Calculate the number of muffins left to sell to hit the target
    muffins_left = target_muffins - total_sales

    # Return the result
    result = muffins_left
    return result

print(solution())