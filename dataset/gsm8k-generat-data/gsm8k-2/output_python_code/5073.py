def solution():
    """Jerry charges $20 to pierce someone's nose and 50% more to pierce their ears. If he pierces 6 noses and 9 ears, how much money does he make?"""
    nose_price = 20
    ear_price = nose_price * 1.5
    total_money = (6 * nose_price) + (9 * ear_price)
    result = total_money
    return result

print(solution())