def solution():
    """Ruth prepared sandwiches. She ate 1 sandwich and gave 2 sandwiches to her brother. Her first cousin arrived and ate 2 sandwiches. Then her two other cousins arrived and ate 1 sandwich each. There were 3 sandwiches left. How many sandwiches did Ruth prepare?"""
    total_sandwiches = 0
    total_sandwiches += 1 # Ruth ate 1 sandwich
    total_sandwiches += 2 # Ruth gave 2 sandwiches to her brother
    total_sandwiches -= 2 # Her first cousin ate 2 sandwiches
    total_sandwiches -= 1 # Her two other cousins ate 1 sandwich each
    total_sandwiches += 3 # There were 3 sandwiches left
    result = total_sandwiches
    return result

print(solution())