def solution():
    """Cynthia harvested 67 potatoes from her garden. After washing them, she cut 13 of them into wedges. She then halved the remaining potatoes and made french fries with one half, and potato chips with the other half. If one potato can be cut into 8 wedges or make 20 potato chips, how many more potato chips than wedges did Cynthia make?"""
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