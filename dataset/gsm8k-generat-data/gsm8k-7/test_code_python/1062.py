def solution():
    # Starting with 1 sandwich that Ruth ate
    num_sandwiches = 1

    # Gave 2 sandwiches to her brother
    num_sandwiches -= 2

    # First cousin ate 2 sandwiches
    num_sandwiches -= 2

    # Two other cousins ate 1 sandwich each
    num_sandwiches -= 1
    num_sandwiches -= 1

    # There were 3 sandwiches left
    num_sandwiches += 3

    result = num_sandwiches
    return result

print(solution())