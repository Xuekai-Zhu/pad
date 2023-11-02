def solution():
    ringo_bands = 3
    mike_bands = 12
    dave_bands = 10
    if ringo_bands > dave_bands and ringo_bands > mike_bands:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())