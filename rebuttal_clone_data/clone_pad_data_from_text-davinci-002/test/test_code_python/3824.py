def solution():
    blonde_hair = 4
    brown_hair = blonde_hair * 4
    black_hair = brown_hair - 2
    black_and_brown = black_hair + brown_hair
    more_black_and_brown = black_and_brown - blonde_hair
    result = more_black_and_brown
    return result

print(solution())