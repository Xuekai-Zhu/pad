def solution():
    # Calculate revenue from pencils with erasers
    eraser_pencil_quantity = 200
    eraser_pencil_price = 0.8
    eraser_pencil_revenue = eraser_pencil_quantity * eraser_pencil_price

    # Calculate revenue from regular pencils
    regular_pencil_quantity = 40
    regular_pencil_price = 0.5
    regular_pencil_revenue = regular_pencil_quantity * regular_pencil_price

    # Calculate revenue from short pencils
    short_pencil_quantity = 35
    short_pencil_price = 0.4
    short_pencil_revenue = short_pencil_quantity * short_pencil_price

    # Calculate total revenue
    total_revenue = eraser_pencil_revenue + regular_pencil_revenue + short_pencil_revenue
    result = total_revenue
    return result

print(solution())