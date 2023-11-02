def solution():
    """Cynthia harvested 67 potatoes from her garden. After washing them, she cut 13 of them into wedges.
    She then halved the remaining potatoes and made french fries with one half, 
    and potato chips with the other half. If one potato can be cut into 8 wedges or make 20 potato chips,
    how many more potato chips than wedges did Cynthia make?"""
    total_potatoes = 67
    wedges = 13
    remaining_potatoes = total_potatoes - wedges
    potato_chips = (remaining_potatoes // 2) * 20
    more_chips_than_wedges = potato_chips - (wedges * 8)
    result = more_chips_than_wedges
    return result

print(solution())