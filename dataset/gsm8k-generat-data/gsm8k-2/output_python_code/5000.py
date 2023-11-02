def solution():
    """Gretchen draws caricatures in the park on the weekends. She charges $20.00 per drawing. If she sold 24 on Saturday and 16 on Sunday, how much money did she make?"""
    saturday_sales = 24
    sunday_sales = 16
    price_per_drawing = 20
    total_sales = (saturday_sales + sunday_sales) * price_per_drawing
    result = total_sales
    return result

print(solution())