def solution():
    total_breaks = 240 // 20 + 240 // 120   # total number of breaks taken
    water_breaks = 240 // 20   # number of water breaks taken
    sitting_breaks = 240 // 120   # number of sitting breaks taken
    difference = water_breaks - sitting_breaks   # difference between water and sitting breaks taken
    result = difference
    return result

print(solution())