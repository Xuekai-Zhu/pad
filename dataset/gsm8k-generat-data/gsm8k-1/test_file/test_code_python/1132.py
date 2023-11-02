def solution():
    """Bob has a certain number of marbles. If he receives 2 dozen more marbles, he will have 60 marbles. If he loses 10 of the marbles he has, how many marbles will Bob have?"""
    marbles_before = (60 - 2 * 12)
    marbles_after = marbles_before - 10
    result = marbles_after
    return result

print(solution())