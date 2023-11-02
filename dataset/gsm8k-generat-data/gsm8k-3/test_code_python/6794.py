def solution():
    """Francis and Kiera had breakfast at a cafe. Muffins cost $2 each, and fruit cups cost $3 each. Francis had 2 muffins and 2 fruit cups. Kiera had 2 muffins and 1 fruit cup. How much did their breakfast cost?"""
    # Define the cost for each item
    MUFFIN_COST = 2
    FRUIT_CUP_COST = 3

    # Calculate Francis's total cost
    francis_cost = (2 * MUFFIN_COST) + (2 * FRUIT_CUP_COST)

    # Calculate Kiera's total cost
    kiera_cost = (2 * MUFFIN_COST) + FRUIT_CUP_COST

    # Calculate the total cost for their breakfast
    total_cost = francis_cost + kiera_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())