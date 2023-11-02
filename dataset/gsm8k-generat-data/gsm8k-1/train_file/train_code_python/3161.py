def solution():
    """If I give my brother 2 marbles I will have double his number of marbles, but my friend will have triple the number I do. The total number of marbles we have together is 63. How many marbles do I have?"""
    total_marbles = 63
    my_marbles = (total_marbles - 2) / 6
    result = my_marbles
    return result

print(solution())