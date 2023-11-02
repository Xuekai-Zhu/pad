def solution():
    """Maddox and Theo both bought 3 Polaroid Cameras, each sold at $20 per camera from Amazon, and decided to sell them on eBay. Maddox sold his cameras at $28 each, while Theo sold his cameras at $23 each. How much more profit did Maddox get from the sale of his cameras than Theo?"""
    # Define the cost and selling price per camera
    COST = 20
    MADDOX_PRICE = 28
    THEO_PRICE = 23

    # Define the number of cameras bought and sold
    cameras_bought = 3
    cameras_sold = 3

    # Calculate Maddox's profit
    maddox_profit = (MADDOX_PRICE - COST) * cameras_sold

    # Calculate Theo's profit
    theo_profit = (THEO_PRICE - COST) * cameras_sold

    # Calculate the difference in profit
    profit_difference = maddox_profit - theo_profit

    # Display the difference in profit
    result = profit_difference
    return result

print(solution())