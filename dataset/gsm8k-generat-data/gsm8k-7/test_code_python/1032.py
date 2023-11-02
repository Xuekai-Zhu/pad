def solution():
    susie_rr = 11
    susie_gc = 6

    brit_rr = susie_rr * 2
    brit_gc = susie_gc / 2

    susie_total = susie_rr + susie_gc
    brit_total = brit_rr + brit_gc

    diff = brit_total - susie_total
    result = diff
    return result

print(solution())