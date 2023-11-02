def solution():
    
    total_potatoes = 67
    wedges_potatoes = 13
    remaining_potatoes = total_potatoes - wedges_potatoes
    french_fries_potatoes = remaining_potatoes / 2
    potato_chips_potatoes = remaining_potatoes / 2
    wedges_count = wedges_potatoes * 8
    chips_count = potato_chips_potatoes * 20
    difference = chips_count - wedges_count
    result = difference
    return result

print(solution())