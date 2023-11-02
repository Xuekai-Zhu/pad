def solution():
    """Cindy had 20 marbles which is 5 more than what Lisa had. If Cindy gave her 12 marbles, how many more marbles does Lisa have now?"""
    cindy_marbles = 20
    lisa_marbles = cindy_marbles - 5
    cindy_marbles -= 12
    lisa_marbles += 12
    difference = lisa_marbles - (cindy_marbles - 5)
    result = difference
    return result

print(solution())