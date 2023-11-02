def solution():
    """Ruth prepared sandwiches. She ate 1 sandwich and gave 2 sandwiches to her brother.
    Her first cousin arrived and ate 2 sandwiches. Then her two other cousins arrived and ate 1 sandwich each.
    There were 3 sandwiches left. How many sandwiches did Ruth prepare?"""
    # Define the number of sandwiches left
    sandwiches_left = 3

    # Calculate the number of sandwiches eaten by the first cousin and the two other cousins
    cousins_eaten = 2 + 1 + 1

    # Calculate the number of sandwiches prepared by Ruth
    sandwiches_prepared = sandwiches_left + cousins_eaten + 1 + 2

    result = sandwiches_prepared
    return result

print(solution())