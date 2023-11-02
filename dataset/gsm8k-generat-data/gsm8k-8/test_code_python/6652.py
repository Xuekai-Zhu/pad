def solution():
    # Define the prices and quantities of each type of pencil
    eraser_pencil_price = 0.8
    regular_pencil_price = 0.5
    short_pencil_price = 0.4

    eraser_pencil_quantity = 200
    regular_pencil_quantity = 40
    short_pencil_quantity = 35

    # Calculate the total revenue from each type of pencil
    eraser_pencil_revenue = eraser_pencil_price * eraser_pencil_quantity
    regular_pencil_revenue = regular_pencil_price * regular_pencil_quantity
    short_pencil_revenue = short_pencil_price * short_pencil_quantity

    # Calculate the total revenue from all pencil sales
    total_revenue = eraser_pencil_revenue + regular_pencil_revenue + short_pencil_revenue
    result = total_revenue
    return result

print(solution())