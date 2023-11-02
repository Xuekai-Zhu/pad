def solution():
    """After eating half of the number of fruits he had, Martin remained with twice as many oranges as limes. If he has 50 oranges now, how many fruits did he initially have?"""
    oranges = 50
    limes = oranges / 2
    remaining_fruits = oranges + limes
    initial_fruits = remaining_fruits * 2
    result = initial_fruits
    return result

print(solution())