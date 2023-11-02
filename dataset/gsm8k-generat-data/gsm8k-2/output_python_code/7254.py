def solution():
    """Fabian has three times more marbles than Kyle and five times more than Miles. If Fabian has 15 marbles, how many marbles do Kyle and Miles have together?"""
    fabian_marbles = 15
    kyle_marbles = fabian_marbles / 3
    miles_marbles = fabian_marbles / 5
    total_marbles = kyle_marbles + miles_marbles
    result = total_marbles
    return result

print(solution())