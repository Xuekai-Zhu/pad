def solution():
    writer = "Charles Dickens"
    religion = "Christian"
    fast_during_ramadan = False
    if religion == "Christian" and not fast_during_ramadan:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())