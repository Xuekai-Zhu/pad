def solution():
    """Jason has three times as many toys as John. If John has 6 more toys than Rachel and Rachel has 1 toy, how many toys does Jason have?"""
    rachel_toys = 1
    john_toys = rachel_toys + 6
    jason_toys = john_toys * 3
    result = jason_toys
    return result

print(solution())