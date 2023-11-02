def solution():
    """Gretchen draws caricatures in the park on the weekends.  She charges $20.00 per drawing.  If she sold 24 on Saturday and 16 on Sunday, how much money did she make?"""
    # Define the price per drawing
    PRICE_PER_DRAWING = 20

    # Define the number of drawings sold on each day
    saturday_drawings = 24
    sunday_drawings = 16

    # Calculate the total amount of money made
    total_money = (saturday_drawings + sunday_drawings) * PRICE_PER_DRAWING

    # Display the total amount of money made
    result = total_money
    return result

print(solution())