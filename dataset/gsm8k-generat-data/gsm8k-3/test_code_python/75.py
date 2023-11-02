def solution():
    """Dale and Andrew had breakfast at a cafe. A slice of toast costs £1, and eggs cost £3 each. Dale had 2 slices of toast and 2 eggs. Andrew had 1 slice of toast and 2 eggs. How much did their breakfast cost?"""
    # Define the prices of toast and eggs
    TOAST_PRICE = 1
    EGG_PRICE = 3

    # Calculate the total cost of Dale's breakfast
    dale_toast_cost = 2 * TOAST_PRICE
    dale_egg_cost = 2 * EGG_PRICE
    dale_breakfast_cost = dale_toast_cost + dale_egg_cost

    # Calculate the total cost of Andrew's breakfast
    andrew_toast_cost = TOAST_PRICE
    andrew_egg_cost = 2 * EGG_PRICE
    andrew_breakfast_cost = andrew_toast_cost + andrew_egg_cost

    # Calculate the total cost of the breakfast
    total_cost = dale_breakfast_cost + andrew_breakfast_cost

    # return the result
    result = total_cost
    return result

print(solution())