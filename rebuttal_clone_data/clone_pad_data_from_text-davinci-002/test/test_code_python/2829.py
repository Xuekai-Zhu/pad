def solution():
    drawings_sold_sat = 24
    drawings_sold_sun = 16
    price_per_drawing = 20
    total_sales = (drawings_sold_sat + drawings_sold_sun) * price_per_drawing
    result = total_sales
    return result

print(solution())