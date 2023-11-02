def solution():
    """Maddie went to a beauty store and bought some beauty products. She bought 3 different makeup palettes which cost $15 each, 4 lipsticks which cost $2.50, and 3 boxes of hair color which cost $4 each. How much did Maddie pay in total?"""
    # Define the cost of each item
    MAKEUP_PALETTE_PRICE = 15
    LIPSTICK_PRICE = 2.5
    HAIR_COLOR_PRICE = 4

    # Define the number of each item purchased
    makeup_palettes = 3
    lipsticks = 4
    hair_color_boxes = 3

    # Calculate the total cost of the makeup palettes
    makeup_palette_cost = makeup_palettes * MAKEUP_PALETTE_PRICE

    # Calculate the total cost of the lipsticks
    lipstick_cost = lipsticks * LIPSTICK_PRICE

    # Calculate the total cost of the hair color boxes
    hair_color_cost = hair_color_boxes * HAIR_COLOR_PRICE

    # Calculate the total cost of all the beauty products
    total_cost = makeup_palette_cost + lipstick_cost + hair_color_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())