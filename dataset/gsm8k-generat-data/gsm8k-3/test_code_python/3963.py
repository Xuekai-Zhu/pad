def solution():
    """9 years from now, John will be 3 times as old as he was 11 years ago. How old is he now?"""
    # Let's assume John's age now is x
    # 9 years from now, John's age will be x+9
    # 11 years ago, John's age was x-11
    # According to the problem, x+9 = 3(x-11)

    x = (3*11 + 9)/2

    # Display John's age
    result = x
    return result

print(solution())