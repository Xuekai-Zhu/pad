def solution():
    sequel_count = 2
    supplemental_works_count = 2
    if sequel_count + supplemental_works_count > 0:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())