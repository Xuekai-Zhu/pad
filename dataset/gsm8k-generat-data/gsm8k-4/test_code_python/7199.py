def solution():
    """For every bike Henry sells, he is paid $8 more than he is paid to paint the bike. If Henry gets $5 to paint the bike, how much does he get paid to sell and paint 8 bikes?"""
    # Define the amount Henry gets paid to paint a bike
    paint_payment = 5

    # Define the additional amount Henry gets paid for each bike he sells
    sales_payment = 8

    # Calculate the total amount Henry gets paid to paint and sell 8 bikes
    total_payment = (paint_payment + paint_payment + sales_payment) * 8

    # Return the result
    result = total_payment
    return result

print(solution())