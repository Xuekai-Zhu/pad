def solution():
    """There's a sale at your favorite "Any item $10" retailer. If you buy 1 shirt you pay $10. If you buy 2, you get the second one at a 50% discount. If you buy 3, you get the third one at a 60% discount. How much money did you save if you bought 3 shirts?"""
    shirt_price = 10
    first_two_shirts_price = shirt_price + shirt_price * 0.5
    third_shirt_price = shirt_price + shirt_price * 0.4
    total_price = first_two_shirts_price + third_shirt_price
    saved_money = 30 - total_price
    result = saved_money
    return result

print(solution())