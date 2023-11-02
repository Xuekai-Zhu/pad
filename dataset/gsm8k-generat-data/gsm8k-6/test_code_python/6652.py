def solution():
    # Calculate the total money made from selling each type of pencil
    eraser_pencil_sales = 0.8 * 200  # Sold 200 eraser pencils for $0.8 each
    regular_pencil_sales = 0.5 * 40  # Sold 40 regular pencils for $0.5 each
    short_pencil_sales = 0.4 * 35  # Sold 35 short pencils for $0.4 each
    total_sales = eraser_pencil_sales + regular_pencil_sales + short_pencil_sales  # Calculate the total sales

    result = total_sales
    return result

print(solution())