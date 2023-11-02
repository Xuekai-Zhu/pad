def solution():
    """$240 was divided between Kelvin and Samuel. Samuel received 3/4 of the money. From his share, Samuel then spent 1/5 of the original $240 on drinks. How much does Samuel have left?"""
    total_money = 240
    samuel_share = (3/4) * total_money
    samuel_spent = (1/5) * total_money
    samuel_left = samuel_share - samuel_spent
    result = samuel_left
    return result

print(solution())