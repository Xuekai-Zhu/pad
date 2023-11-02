def solution():
    """Steven has 4 times as many shirts as Andrew. Andrew has 6 times as many shirts as Brian. If Brian has 3 shirts, how many does Steven have?"""
    brian_shirts = 3
    andrew_shirts = brian_shirts * 6
    steven_shirts = andrew_shirts * 4
    result = steven_shirts
    return result

print(solution())