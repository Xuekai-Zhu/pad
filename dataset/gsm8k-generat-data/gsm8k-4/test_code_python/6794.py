def solution():
    """Francis and Kiera had breakfast at a cafe. Muffins cost $2 each, and fruit cups cost $3 each. Francis had 2 muffins and 2 fruit cups. Kiera had 2 muffins and 1 fruit cup. How much did their breakfast cost?"""
    # Define the prices of muffins and fruit cups
    MUFFIN_PRICE = 2
    FRUIT_CUP_PRICE = 3

    # Calculate the cost of Francis' breakfast
    francis_cost = (2 * MUFFIN_PRICE) + (2 * FRUIT_CUP_PRICE)

    # Calculate the cost of Kiera's breakfast
    kiera_cost = (2 * MUFFIN_PRICE) + (1 * FRUIT_CUP_PRICE)

    # Calculate the total cost of their breakfast
    total_cost = francis_cost + kiera_cost

    result = total_cost
    return result

print(solution())