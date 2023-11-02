def solution():
    """Ruth prepared sandwiches. She ate 1 sandwich and gave 2 sandwiches to her brother. Her first cousin arrived and ate 2 sandwiches. Then her two other cousins arrived and ate 1 sandwich each. There were 3 sandwiches left. How many sandwiches did Ruth prepare?"""
    sandwiches_left = 3
    sandwiches_consumed = 1 + 2 + 2 + 1 + 1
    sandwiches_prepared = sandwiches_left + sandwiches_consumed
    result = sandwiches_prepared
    return result

print(solution())