def solution():
    """The basketball team is practicing their free-throws, making as many as they can in one minute. DeShawn made 12 free-throws, and Kayla made 50% more than DeShawn. If Annieka made 4 fewer than Kayla, how many did Annieka make?"""
    # DeShawn's free-throws
    deshawn = 12

    # Kayla's free-throws
    kayla = deshawn * 1.5

    # Annieka's free-throws
    annieka = kayla - 4

    # return the result
    result = annieka
    return result

print(solution())