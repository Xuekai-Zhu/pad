def solution():
    """In five years Sam will be 3 times as old as Drew. If Drew is currently 12 years old, how old is Sam?"""
    drew_age = 12
    sam_age = 3 * (drew_age + 5) - 5
    result = sam_age
    return result

print(solution())