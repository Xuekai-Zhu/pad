def solution():
    James_meal = 16
    Friend_meal = 14
    tip = 0.2 # 20% tip
    tip_amount = (James_meal + Friend_meal) * tip / 2
    James_half = James_meal / 2 + tip_amount
    result = James_half
    return result

print(solution())