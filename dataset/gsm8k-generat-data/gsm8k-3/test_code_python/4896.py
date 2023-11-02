def solution():
    """Grover bought 3 boxes of face masks. He plans to sell them for $0.50 each. If each box has 20 face masks, and he bought the 3 boxes for $15, how much will be his total profit?"""
    # Define the cost of a box of face masks and the selling price per mask
    BOX_COST = 15
    MASK_PRICE = 0.5

    # Define the number of masks per box
    MASKS_PER_BOX = 20

    # Calculate the total cost of the boxes of face masks
    total_cost = BOX_COST

    # Calculate the total revenue from selling the face masks
    total_revenue = MASK_PRICE * (3 * MASKS_PER_BOX)

    # Calculate the total profit
    total_profit = total_revenue - total_cost

    # Display the total profit
    result = total_profit
    return result

print(solution())