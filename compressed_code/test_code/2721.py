def solution():
    
    plates_price = 2
    plates_count = 9
    plates_total = plates_price * plates_count
    total_price = 24
    spoons_price = 1.5
    spoons_total = total_price - plates_total
    spoons_count = spoons_total / spoons_price
    result = spoons_count
    return result

print(solution())