def solution():
    # Find the number of students who didn't bomb their finals
    not_bombed = 3/4 * 180

    # Find the number of students who showed up to take the test
    showed_up = 2/3 * not_bombed

    # Find the number of students who got at least a D
    at_least_D = not_bombed - showed_up - 20

    # Find the number of students who passed their finals
    passed = showed_up - at_least_D

    result = passed
    return result

print(solution())