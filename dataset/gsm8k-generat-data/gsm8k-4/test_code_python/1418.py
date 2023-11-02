def solution():
    """Maria wants to paint a picture and needs some tools to do that. She wants to buy a set of brushes for $20 and some canvas for three times more than the brushes. The paint costs Maria $8 per liter, and she needs at least 5 liters. How much money will she earn on the painting if she will be able to sell it for $200?"""
    # Define the cost of the brushes
    brushes_cost = 20

    # Define the cost of the canvas
    canvas_cost = brushes_cost * 3

    # Define the cost of the paint
    paint_cost = 8 * 5

    # Define the total cost of all the tools
    total_cost = brushes_cost + canvas_cost + paint_cost

    # Define the selling price of the painting
    selling_price = 200

    # Calculate the profit from selling the painting
    profit = selling_price - total_cost

    # Return the result
    result = profit
    return result

print(solution())