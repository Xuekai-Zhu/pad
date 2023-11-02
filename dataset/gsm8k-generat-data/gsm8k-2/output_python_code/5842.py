def solution():
    """Sally had 14 fries at lunch. Her friend Mark gave her one-third of his 36 fries at lunch. How many fries did Sally have for lunch after that?"""
    sally_fries = 14
    mark_fries = 36
    sally_fries += mark_fries / 3
    result = sally_fries
    return result

print(solution())