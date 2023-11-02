def solution():
    # Define the number of pencils sold and the total amount earned
    pencils_sold = 20
    total_earned = 80

    # Determine the price of each pencil
    pencil_price = total_earned / pencils_sold

    # Determine the price of two erasers
    eraser_price = pencil_price / 2

    result = eraser_price
    return result

print(solution())