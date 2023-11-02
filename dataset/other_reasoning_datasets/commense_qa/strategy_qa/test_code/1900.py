def solution():
    hugh_commonalities = {"writer", "lawyer", "judge"}
    judith_commonalities = {"judge", "lawyer", "author"}
    commonalities = hugh_commonalities.intersection(judith_commonalities)
    if commonalities:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())