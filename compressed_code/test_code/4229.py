def solution():
    
    cows = 20
    pigs = 4 * cows
    pig_price = 400
    cow_price = 800
    total_earnings = pigs * pig_price + cows * cow_price
    result = total_earnings
    return result

print(solution())