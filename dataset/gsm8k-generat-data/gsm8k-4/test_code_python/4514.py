def solution():
    """Betty ordered 18 items in an online shop via cash on delivery. She ordered 6 pieces of slippers that cost $2.5 each, 4 pieces of lipstick for $1.25 each, and 8 pieces of hair color for $3 each. How much did Betty pay in total when it was delivered?"""
    # Calculate the total cost of the slippers
    slippers_cost = 6 * 2.5

    # Calculate the total cost of the lipstick
    lipstick_cost = 4 * 1.25

    # Calculate the total cost of the hair color
    hair_color_cost = 8 * 3

    # Calculate the total cost of all items
    total_cost = slippers_cost + lipstick_cost + hair_color_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())