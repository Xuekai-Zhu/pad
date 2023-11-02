def solution():
    """Royce takes 40 minutes more than double Rob to shingle a house. If Rob takes 2 hours, how many minutes does Royce take?"""
    rob_time = 2 * 60  # convert hours to minutes
    royce_time = rob_time * 2 + 40
    result = royce_time
    return result

print(solution())