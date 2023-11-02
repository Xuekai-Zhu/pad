def solution():
    """For every bike Henry sells, he is paid $8 more than he is paid to paint the bike. If Henry gets $5 to paint the bike, how much does he get paid to sell and paint 8 bikes?"""
    # Define the amount Henry gets paid to paint a bike
    PAINT_PAY = 5

    # Calculate the amount Henry gets paid to sell a bike
    SELL_PAY = PAINT_PAY + 8

    # Calculate Henry's total earnings for selling and painting 8 bikes
    total_earnings = 8 * (PAINT_PAY + SELL_PAY)

    # Display Henry's total earnings
    result = total_earnings
    return result

print(solution())