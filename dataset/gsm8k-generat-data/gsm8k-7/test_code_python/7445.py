def solution():
    num_people = 50

    # At first stop, 15 people get off
    num_people -= 15

    # At second stop, 8 people get off and 2 get on
    num_people -= 8
    num_people += 2

    # At third stop, 4 people get off and 3 get on
    num_people -= 4
    num_people += 3

    result = num_people
    return result

print(solution())