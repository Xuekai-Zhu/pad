def solution():
    
    red_price = 20000
    green_percentage = 0.2
    red_bonus = red_price * 0.1 * 2
    total_green_bonus = 7000 - red_bonus
    green_bonus_per_tractor = total_green_bonus / 3
    green_price = green_bonus_per_tractor / green_percentage
    result = green_price
    return result

print(solution())