def solution():
    old_barbell_price = 250
    increase_percentage = 0.3
    new_barbell_price = old_barbell_price * (1 + increase_percentage)
    result = new_barbell_price
    return result

print(solution())