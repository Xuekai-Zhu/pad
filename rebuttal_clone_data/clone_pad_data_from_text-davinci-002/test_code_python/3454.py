def solution():
    initial_enrollment = 8
    new_enrollment = 8 + (8 * .25) - 2 + (5 * initial_enrollment) - 2 + 6 - (initial_enrollment * .5)
    result = new_enrollment
    return result

print(solution())