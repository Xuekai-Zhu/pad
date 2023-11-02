def solution():
    """In a stationery store, there are three kinds of pencils. A pencil with an eraser, which costs $0.8 each, a regular pencil for $0.5 each, and a short pencil for $0.4 each. This store was able to sell 200 pencils with an eraser, 40 regular pencils, and 35 short pencils. How much money did the store make from these sales?"""
    # Define the prices and quantities of each type of pencil
    eraser_price = 0.8
    eraser_qty = 200
    regular_price = 0.5
    regular_qty = 40
    short_price = 0.4
    short_qty = 35

    # Calculate the total revenue from each type of pencil
    eraser_revenue = eraser_price * eraser_qty
    regular_revenue = regular_price * regular_qty
    short_revenue = short_price * short_qty

    # Calculate the total revenue from all sales
    total_revenue = eraser_revenue + regular_revenue + short_revenue

    result = total_revenue
    return result

print(solution())