def solution():
    """A store sells pencils and erasers. It has a rule that for every pencil you buy, you must buy 2 erasers which cost 1/2 the price of the pencils. If they sold 20 pencils and earned $80, how much do erasers cost?"""
    # Define the number of pencils sold and the total earnings
    pencils_sold = 20
    total_earnings = 80

    # Calculate the cost of each pencil
    pencil_cost = total_earnings / pencils_sold

    # Calculate the cost of each eraser
    eraser_cost = 0.5 * pencil_cost

    # Display the cost of each eraser
    result = eraser_cost
    return result

print(solution())