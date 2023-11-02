def solution():
    stickers_brought = 50
    stickers_given = 4 * 5 + 2 * (50 - 5)
    stickers_leftover = 50 - stickers_given
    students = (stickers_leftover + 8) / 2
    result = students
    return result

print(solution())