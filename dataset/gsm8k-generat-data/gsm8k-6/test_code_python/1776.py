def solution():
    # Find the total score before William took the test
    total_score = 74 * 30  
    # Find the minimum score that William needs to get
    required_score = (0.75 * (30 + 1)) * 100 - total_score  
    result = required_score
    return result

print(solution())