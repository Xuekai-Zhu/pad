def solution():
    """Maria wants to paint a picture and needs some tools to do that. She wants to buy a set of brushes for $20 and some canvas for three times more than the brushes. The paint costs Maria $8 per liter, and she needs at least 5 liters. How much money will she earn on the painting if she will be able to sell it for $200?"""
    # Define the cost of the brushes, canvas and paint
    BRUSHES_COST = 20
    CANVAS_COST = BRUSHES_COST * 3
    PAINT_COST = 8

    # Define the amount of paint needed (at least 5 liters)
    PAINT_AMOUNT = 5

    # Calculate the cost of the tools
    tools_cost = BRUSHES_COST + CANVAS_COST

    # Calculate the cost of the paint
    paint_cost = PAINT_AMOUNT * PAINT_COST

    # Calculate the total cost of the painting
    total_cost = tools_cost + paint_cost

    # Calculate Maria's earnings
    earnings = 200 - total_cost

    # Display Maria's earnings
    result = earnings
    return result

print(solution())