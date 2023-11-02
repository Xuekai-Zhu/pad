def solution():
    """Dale and Andrew had breakfast at a cafe. A slice of toast costs £1, and eggs cost £3 each. Dale had 2 slices of toast and 2 eggs. Andrew had 1 slice of toast and 2 eggs. How much did their breakfast cost?"""
    # Define the prices of toast and eggs
    TOAST_PRICE = 1
    EGG_PRICE = 3

    # Calculate the total cost of Dale's breakfast
    dale_cost = 2*TOAST_PRICE + 2*EGG_PRICE

    # Calculate the total cost of Andrew's breakfast
    andrew_cost = 1*TOAST_PRICE + 2*EGG_PRICE

    # Calculate the total cost of their breakfast
    total_cost = dale_cost + andrew_cost

    # return the result
    result = total_cost
    return result

print(solution())