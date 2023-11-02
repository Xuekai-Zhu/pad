def solution():
    """Every time Janet folds her blanket its thickness doubles. If it starts out 3 inches thick, how thick will it be after 4 foldings?"""
    thickness = 3
    for i in range(4):
        thickness *= 2

    result = thickness
    return result

print(solution())