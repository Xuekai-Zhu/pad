def solution():
    
    total_pens = 20 * 5
    pens_given_friends = int(total_pens * 0.4)
    pens_left = total_pens - pens_given_friends
    pens_given_classmates = pens_left // 4
    pens_left -= pens_given_classmates
    result = pens_left
    return result

print(solution())