def solution():
    saturday_drawings = 24  # Gretchen sold 24 drawings on Saturday
    sunday_drawings = 16  # Gretchen sold 16 drawings on Sunday
    price_per_drawing = 20.00  # Gretchen charges $20.00 per drawing

    # Calculate the total amount of money Gretchen made
    total_income = (saturday_drawings + sunday_drawings) * price_per_drawing
    result = total_income
    return result

print(solution())