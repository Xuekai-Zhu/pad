def solution():
    """Sherry is making banana bread for a bake sale. She wants to make 99 loaves. Her recipe makes enough batter for 3 loaves. The recipe calls for 1 banana. How many bananas does Sherry need?"""
    # Define the number of loaves and the amount of batter per loaf
    loaves = 99
    batter_per_loaf = 1/3

    # Calculate the total amount of batter needed
    total_batter = loaves * batter_per_loaf

    # Calculate the number of bananas needed
    bananas = total_batter

    # Return the result rounded to the nearest whole number
    result = round(bananas)
    return result

print(solution())