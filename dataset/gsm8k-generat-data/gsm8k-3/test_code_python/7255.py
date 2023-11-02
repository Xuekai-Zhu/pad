def solution():
    """Fabian has three times more marbles than Kyle and five times more than Miles. If Fabian has 15 marbles, how many marbles do Kyle and Miles have together?"""
    # Define the number of marbles Fabian has
    fabian_marbles = 15

    # Calculate the number of marbles Kyle has
    kyle_marbles = fabian_marbles / 3

    # Calculate the number of marbles Miles has
    miles_marbles = fabian_marbles / 5

    # Calculate the total number of marbles Kyle and Miles have together
    total_marbles = kyle_marbles + miles_marbles

    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())