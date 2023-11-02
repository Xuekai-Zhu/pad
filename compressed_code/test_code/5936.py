def solution():
    
    num_people = 16
    num_rolls = 40
    rolls_half1 = (num_people // 2) * 1.5
    rolls_half2 = (num_people // 2) * 0.5
    total_rolls = rolls_half1 + rolls_half2
    leftover_rolls = num_rolls - total_rolls
    result = leftover_rolls
    return result

print(solution())