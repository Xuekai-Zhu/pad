def solution():
    
    monday_price = 5
    wednesday_price = monday_price * 2
    saturday_price = monday_price * 5
    glenn_spends = (1 * wednesday_price) + (1 * saturday_price)
    result = glenn_spends
    return result

print(solution())