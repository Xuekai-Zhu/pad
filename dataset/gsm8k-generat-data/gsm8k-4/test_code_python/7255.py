def solution():
    """Fabian has three times more marbles than Kyle and five times more than Miles. If Fabian has 15 marbles, how many marbles do Kyle and Miles have together?"""
    # Define the number of marbles Fabian has
    fabian_marbles = 15

    # Calculate the ratio of marbles between Fabian, Kyle, and Miles
    fabian_ratio = 1
    kyle_ratio = fabian_ratio / 3
    miles_ratio = fabian_ratio / 5

    # Calculate the total ratio and use it to find their respective marble counts
    total_ratio = fabian_ratio + kyle_ratio + miles_ratio
    kyle_marbles = kyle_ratio / total_ratio * fabian_marbles
    miles_marbles = miles_ratio / total_ratio * fabian_marbles

    # Calculate the sum of Kyle and Miles' marble counts
    total_marbles = kyle_marbles + miles_marbles

    # Return the result
    result = total_marbles
    return result

print(solution())