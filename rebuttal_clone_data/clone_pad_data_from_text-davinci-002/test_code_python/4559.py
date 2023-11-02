def solution():
    pounds_marina = 4.5
    ounces_lazlo = 6
    ounces_marina = ounces_lazlo + (pounds_marina * 16)
    result = ounces_marina - (ounces_lazlo + (pounds_marina * 16))
    return result

print(solution())