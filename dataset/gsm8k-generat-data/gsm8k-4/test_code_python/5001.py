def solution():
    """Gretchen draws caricatures in the park on the weekends. She charges $20.00 per drawing. If she sold 24 on Saturday and 16 on Sunday, how much money did she make?"""
    # Define the price per drawing and the number of drawings sold on each day
    PRICE_PER_DRAWING = 20
    SATURDAY_DRAWINGS = 24
    SUNDAY_DRAWINGS = 16

    # Calculate the total earnings from Saturday and Sunday
    saturday_earnings = SATURDAY_DRAWINGS * PRICE_PER_DRAWING
    sunday_earnings = SUNDAY_DRAWINGS * PRICE_PER_DRAWING

    # Calculate the total earnings for the entire weekend
    total_earnings = saturday_earnings + sunday_earnings

    # Return the total earnings
    result = total_earnings
    return result

print(solution())