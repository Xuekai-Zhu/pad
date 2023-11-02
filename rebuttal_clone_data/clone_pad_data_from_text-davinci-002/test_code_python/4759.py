def solution():
    old_barbell_price = 250
    percent_increase = 30
    increase_amount = old_barbell_price * (percent_increase / 100)
    new_barbell_price = old_barbell_price + increase_amount
    result = new_barbell_price
    return result

print(solution())