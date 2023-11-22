def solution():
    
    roses = 15
    rose_price = 2
    dozen_price = 15
    total_cost = (roses * rose_price) + (dozen_price * 12)
    total_paid = 5 * 100
    remaining_money = total_paid - total_cost
    quarters = remaining_money / 0.25
    result = quarters
    return result

print(solution())