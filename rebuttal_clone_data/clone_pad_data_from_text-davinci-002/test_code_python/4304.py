def solution():
    rachels_age = 12
    grandfathers_age = 7 * rachels_age
    mothers_age = grandfathers_age / 2
    fathers_age = mothers_age + 5
    when_rachel_is_25 = fathers_age + 13
    result = when_rachel_is_25
    return result

print(solution())