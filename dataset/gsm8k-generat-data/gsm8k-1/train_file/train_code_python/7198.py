def solution():
    """For every bike Henry sells, he is paid $8 more than he is paid to paint the bike. If Henry gets $5 to paint the bike, how much does he get paid to sell and paint 8 bikes?"""
    payment_for_painting = 5
    payment_for_selling = payment_for_painting + 8
    num_bikes = 8
    total_payment = (num_bikes * payment_for_painting) + (num_bikes * payment_for_selling)
    result = total_payment
    return result

print(solution())