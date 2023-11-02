def solution():
    hattie_first = 180
    lorelei_first = hattie_first * 3/4
    hattie_second = hattie_first + 50
    lorelei_second = lorelei_first + 50
    total_jumps = hattie_first + hattie_second + lorelei_first + lorelei_second
    result = total_jumps
    return result

print(solution())