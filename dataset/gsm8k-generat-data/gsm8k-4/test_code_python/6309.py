def solution():
    """Maddox and Theo both bought 3 Polaroid Cameras, each sold at $20 per camera from Amazon, and decided to sell them on eBay. Maddox sold his cameras at $28 each, while Theo sold his cameras at $23 each. How much more profit did Maddox get from the sale of his cameras than Theo?"""
    # Define the initial cost and selling price of the cameras
    COST_PER_CAMERA = 20
    SELLING_PRICE_MADDOX = 28
    SELLING_PRICE_THEO = 23

    # Calculate the cost and revenue for Maddox's cameras
    cost_maddox = 3 * COST_PER_CAMERA
    revenue_maddox = 3 * SELLING_PRICE_MADDOX

    # Calculate the profit Maddox made
    profit_maddox = revenue_maddox - cost_maddox

    # Calculate the cost and revenue for Theo's cameras
    cost_theo = 3 * COST_PER_CAMERA
    revenue_theo = 3 * SELLING_PRICE_THEO

    # Calculate the profit Theo made
    profit_theo = revenue_theo - cost_theo

    # Calculate the difference in profit between Maddox and Theo
    difference = profit_maddox - profit_theo

    # return the result
    result = difference
    return result

print(solution())