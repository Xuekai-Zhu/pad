def solution():
    eraser_pencil_price = 0.8
    regular_pencil_price = 0.5
    short_pencil_price = 0.4

    num_eraser_pencils_sold = 200
    num_regular_pencils_sold = 40
    num_short_pencils_sold = 35

    # Calculate the total revenue from selling eraser pencils
    eraser_pencils_revenue = eraser_pencil_price * num_eraser_pencils_sold

    # Calculate the total revenue from selling regular pencils
    regular_pencils_revenue = regular_pencil_price * num_regular_pencils_sold

    # Calculate the total revenue from selling short pencils
    short_pencils_revenue = short_pencil_price * num_short_pencils_sold

    # Calculate the total revenue from all pencil sales
    total_revenue = eraser_pencils_revenue + regular_pencils_revenue + short_pencils_revenue
    result = total_revenue
    return result

print(solution())