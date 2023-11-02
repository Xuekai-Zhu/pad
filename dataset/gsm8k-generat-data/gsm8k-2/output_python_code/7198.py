def solution():
    """For every bike Henry sells, he is paid $8 more than he is paid to paint the bike. If Henry gets $5 to paint the bike, how much does he get paid to sell and paint 8 bikes?"""
    paint_payment = 5
    sell_payment = paint_payment + 8
    total_payment = (8 * sell_payment) + (8 * paint_payment)
    result = total_payment
    return result

print(solution())