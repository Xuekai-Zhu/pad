def solution():
    passengers = 0

    # At the first stop, 7 people got on
    passengers += 7

    # At the second stop, 3 people got off and 5 people got on
    passengers -= 3
    passengers += 5

    # At the third stop, 2 people got off and 4 people got on
    passengers -= 2
    passengers += 4

    result = passengers
    return result

print(solution())