def solution():
    
    total_oranges = 25
    bad_oranges = total_oranges * 0.2
    unripe_oranges = total_oranges * 0.2
    sour_oranges = 2
    good_oranges = total_oranges - bad_oranges - unripe_oranges - sour_oranges
    result = good_oranges
    return result

print(solution())