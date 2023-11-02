def solution():
    """Grant scored 10 points higher on his math test than John. John received twice as many points as Hunter who scored a 45 on his math test. What was Grant's test score?"""
    # Define Hunter's math test score
    hunter_score = 45

    # Calculate John's math test score
    john_score = hunter_score * 2

    # Calculate Grant's math test score
    grant_score = john_score + 10

    # return the result
    result = grant_score
    return result

print(solution())