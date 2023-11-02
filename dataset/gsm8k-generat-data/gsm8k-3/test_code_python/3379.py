def solution():
    """On a quiz, Nicole answered 3 fewer questions correctly than Kim, and Kim answered 8 more questions correctly than Cherry. If Nicole answered 22 correctly, how many did Cherry answer correctly?"""
    # Let's use variables to represent the number of questions Cherry, Kim, and Nicole answered correctly
    # Let c be the number of questions Cherry answered correctly
    # Let k be the number of questions Kim answered correctly
    # Let n be the number of questions Nicole answered correctly

    # We know from the problem that Nicole answered 3 fewer than Kim, so:
    # n = k - 3

    # We also know that Kim answered 8 more than Cherry, so:
    # k = c + 8

    # Finally, we know that Nicole answered 22 correctly, so:
    # n = 22

    # Substituting n and k in terms of c, we have:
    # 22 = k - 3
    # k = 25
    # 25 = c + 8
    # c = 17

    # Therefore, Cherry answered 17 questions correctly.
    result = 17
    return result

print(solution())