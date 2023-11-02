def solution():
    
    total_pens = 20 * 5
    friends_pens = 0.4 * total_pens
    remaining_pens = total_pens - friends_pens
    classmates_pens = remaining_pens / 4
    pens_left = remaining_pens - classmates_pens
    result = pens_left
    return result

print(solution())