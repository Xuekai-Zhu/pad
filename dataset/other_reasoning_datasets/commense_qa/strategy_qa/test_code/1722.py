def solution():
    lowest_rank = "white belt"
    jon_jones_rank = "purple belt"
    if jon_jones_rank > lowest_rank:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())