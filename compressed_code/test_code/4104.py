def solution():
    
    shirt_price = 1
    pants_price = 3
    num_shirts = 5
    num_pants = 5
    total_earned = (shirt_price * num_shirts) + (pants_price * num_pants)
    half_earned = total_earned / 2
    remaining_money = total_earned - half_earned
    result = remaining_money
    return result

print(solution())