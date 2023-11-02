def solution():
    """Jerry charges $20 to pierce someone's nose and 50% more to pierce their ears. If he pierces 6 noses and 9 ears, how much money does he make?"""
    nose_price = 20
    ear_price = nose_price * 1.5
    noses_pierced = 6
    ears_pierced = 9
    
    total_money = (nose_price * noses_pierced) + (ear_price * ears_pierced)
    result = total_money
    return result

print(solution())