def solution():
    
    total_roses = 3 * 12
    roses_given_away = total_roses / 2
    roses_in_vase = total_roses - roses_given_away
    wilted_roses = roses_in_vase / 3
    remaining_roses = roses_in_vase - wilted_roses
    result = remaining_roses
    return result

print(solution())