def solution():
    """$240 was divided between Kelvin and Samuel. Samuel received 3/4 of the money. From his share, Samuel then spent 1/5 of the original $240 on drinks. How much does Samuel have left?"""
    total_money = 240
    samuel_percent = 3/4
    samuel_money = total_money * samuel_percent
    drinks_percent = 1/5
    drinks_cost = total_money * drinks_percent
    samuel_left = samuel_money - drinks_cost
    result = samuel_left
    return result

print(solution())