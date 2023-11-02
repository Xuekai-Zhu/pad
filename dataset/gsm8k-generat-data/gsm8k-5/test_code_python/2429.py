def solution():
    bea_price = 25  # Bea sells her lemonade at 25 cents per glass
    dawn_price = 28  # Dawn sells her lemonade at 28 cents per glass
    bea_glasses_sold = 10  # Bea sold 10 glasses
    dawn_glasses_sold = 8  # Dawn sold 8 glasses

    # Calculate the total earnings of Bea and Dawn
    bea_earnings = bea_price * bea_glasses_sold
    dawn_earnings = dawn_price * dawn_glasses_sold

    # Calculate the difference in earnings between Bea and Dawn
    difference = bea_earnings - dawn_earnings
    result = difference
    return result

print(solution())