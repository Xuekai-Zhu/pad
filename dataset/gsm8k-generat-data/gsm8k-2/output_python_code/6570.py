def solution():
    """Sally, Sam, and Steve went to play with their marbles. In the beginning, Sam has twice as many marbles as Steve while Sally has 5 less than Sam. After Sam has given Sally and Steve 3 marbles each, Sam has 8 marbles left. How many marbles does Steve have now?"""
    sam = 2 * steve
    sally = sam - 5
    sam -= 6
    sally += 3
    steve += 3
    sam_left = 8
    total_marbles = sam_left + sally + steve
    result = steve
    return result

print(solution())