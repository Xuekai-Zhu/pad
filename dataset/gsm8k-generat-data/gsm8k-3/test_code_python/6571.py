def solution():
    """Sally, Sam, and Steve went to play with their marbles. In the beginning, Sam has twice as many marbles as Steve while Sally has 5 less than Sam. After Sam has given Sally and Steve 3 marbles each, Sam has 8 marbles left. How many marbles does Steve have now?"""
    # Let's start by defining variables to represent the number of marbles each child has
    steve_marbles = x
    sam_marbles = 2*x
    sally_marbles = 2*x - 5

    # After Sam gives away 3 marbles to each child, he is left with 8 marbles
    sam_marbles -= 6 # 2*3 = 6
    sam_marbles = 8

    # Now we can solve for x to find how many marbles Steve has
    x = 4
    steve_marbles = x

    # Display the number of marbles Steve has now
    result = steve_marbles
    return result

print(solution())