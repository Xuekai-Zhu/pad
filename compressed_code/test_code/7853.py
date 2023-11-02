def solution():
    
    litter_size = 8
    given_away = litter_size / 2
    remaining = litter_size - given_away - 1
    sale_price = 600
    stud_fee = 300
    profit = (remaining * sale_price) - stud_fee
    result = profit
    return result

print(solution())