def solution():
    bonus = 1496
    kitchen = bonus / 22
    holidays = bonus / 4
    Christmas = bonus / 8
    leftover = bonus - (kitchen + holidays + Christmas)
    result = leftover
    return result

print(solution())