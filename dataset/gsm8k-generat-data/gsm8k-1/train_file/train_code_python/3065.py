def solution():
    """After eating half of the number of fruits he had, Martin remained with twice as many oranges as limes. If he has 50 oranges now, how many fruits did he initially have?"""
    oranges = 50
    oranges_limes_ratio = 2
    limes = oranges / oranges_limes_ratio
    remaining_fruits = oranges + limes
    initially_had = remaining_fruits * 2
    result = initially_had
    return result

print(solution())