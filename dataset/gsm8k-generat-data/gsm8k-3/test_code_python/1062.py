def solution():
    """Ruth prepared sandwiches. She ate 1 sandwich and gave 2 sandwiches to her brother. Her first cousin arrived and ate 2 sandwiches. Then her two other cousins arrived and ate 1 sandwich each. There were 3 sandwiches left. How many sandwiches did Ruth prepare?"""
    # Define the total number of sandwiches prepared
    total_sandwiches = 0

    # Ruth prepared some sandwiches
    total_sandwiches += 1

    # Ruth gave some sandwiches to her brother
    total_sandwiches -= 2

    # Ruth's first cousin arrived and ate some sandwiches
    total_sandwiches -= 2

    # Ruth's two other cousins arrived and ate some sandwiches
    total_sandwiches -= 1
    total_sandwiches -= 1

    # There were 3 sandwiches left
    total_sandwiches += 3

    # Display the total number of sandwiches prepared
    result = total_sandwiches
    return result

print(solution())