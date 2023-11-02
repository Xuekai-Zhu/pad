def solution():
    calen_start = 2*candy_start + 3
    caleb_start = calen_start - 5
    calen_final = 10
    calen_lost = calen_start - calen_final
    caleb_final = caleb_start - calen_lost
    candy_final = (caleb_final + 3) / 2
    result = candy_final
    return result

print(solution())