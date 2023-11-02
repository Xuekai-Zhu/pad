def solution():
    saturday_sales = 24
    sunday_sales = 16
    price_per_drawing = 20.00

    # Calculate the total sales on Saturday
    saturday_total = saturday_sales * price_per_drawing

    # Calculate the total sales on Sunday
    sunday_total = sunday_sales * price_per_drawing

    # Calculate the total money Gretchen made over the weekend
    total_sales = saturday_total + sunday_total
    result = total_sales
    return result

print(solution())