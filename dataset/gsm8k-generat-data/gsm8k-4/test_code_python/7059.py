def solution():
    """Maddie went to a beauty store and bought some beauty products. She bought 3 different makeup palettes which cost $15 each, 4 lipsticks which cost $2.50, and 3 boxes of hair color which cost $4 each. How much did Maddie pay in total?"""
    # Define the prices of each product
    palette_price = 15
    lipstick_price = 2.5
    hair_color_price = 4

    # Calculate the total cost of the makeup palettes
    palette_cost = 3 * palette_price

    # Calculate the total cost of the lipsticks
    lipstick_cost = 4 * lipstick_price

    # Calculate the total cost of the hair color
    hair_color_cost = 3 * hair_color_price

    # Calculate the total cost of all the beauty products
    total_cost = palette_cost + lipstick_cost + hair_color_cost

    # Return the result
    result = total_cost
    return result

print(solution())