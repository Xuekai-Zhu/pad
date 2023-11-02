def solution():
    """Betty ordered 18 items in an online shop via cash on delivery. She ordered 6 pieces of slippers that cost $2.5 each, 4 pieces of lipstick for $1.25 each, and 8 pieces of hair color for $3 each. How much did Betty pay in total when it was delivered?"""
    # Define the prices of each item
    SLIPPERS_PRICE = 2.5
    LIPSTICK_PRICE = 1.25
    HAIR_COLOR_PRICE = 3

    # Define the quantities of each item
    slippers_quantity = 6
    lipstick_quantity = 4
    hair_color_quantity = 8

    # Calculate the total cost of the slippers
    slippers_cost = slippers_quantity * SLIPPERS_PRICE

    # Calculate the total cost of the lipstick
    lipstick_cost = lipstick_quantity * LIPSTICK_PRICE

    # Calculate the total cost of the hair color
    hair_color_cost = hair_color_quantity * HAIR_COLOR_PRICE

    # Calculate the total cost of all the items
    total_cost = slippers_cost + lipstick_cost + hair_color_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())