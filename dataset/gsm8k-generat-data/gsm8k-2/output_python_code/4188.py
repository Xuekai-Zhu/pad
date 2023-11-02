def solution():
    """In eight years, Mr. Bernard will be 3 times as old as Luke is now. If Luke is 20, what is 10 years less than their average age?"""
    luke_age = 20
    bernard_age = (luke_age * 3) + 8
    total_age = luke_age + bernard_age
    average_age = total_age / 2
    result = average_age - 10
    return result

print(solution())