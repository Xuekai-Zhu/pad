def solution():
    """A store sells pencils and erasers. It has a rule that for every pencil you buy, you must buy 2 erasers which cost 1/2 the price of the pencils. If they sold 20 pencils and earned $80, how much do erasers cost?"""
    # Define the number of pencils sold and the earnings
    pencils_sold = 20
    earnings = 80

    # Calculate the price of one pencil
    pencil_price = earnings / pencils_sold

    # Calculate the price of two erasers
    erasers_price = pencil_price / 2

    # return the result
    result = erasers_price
    return result

print(solution())