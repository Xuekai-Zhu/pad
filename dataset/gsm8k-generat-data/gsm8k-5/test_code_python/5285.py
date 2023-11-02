def solution():
    stones = 40  # Given in the question
    trees = 3 * stones  # Number of trees is three times more than the number of stones
    total_objects = stones + trees  # Total number of objects in the courtyard
    birds = 2 * total_objects  # Twice the number of objects in the courtyard

    result = birds
    return result

print(solution())