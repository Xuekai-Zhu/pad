def solution():
    monogamous_pairs_with_same_sex = 0.25
    monogamous_pairs_with_extra_paternity = 0.33
    if monogamous_pairs_with_same_sex < 1 and monogamous_pairs_with_extra_paternity > 0:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())