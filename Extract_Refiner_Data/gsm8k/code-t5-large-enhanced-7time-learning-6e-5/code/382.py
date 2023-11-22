def solution():
    
    # Define the total number of tests and the desired scores
    total_tests = 65 + 94 + 81 + 86 + 74
    desired_scores = 80

    # Calculate the current math grade based on the desired scores
    current_grade = (desired_scores * 5) / total_tests

    # return the result
    result = current_grade
    return result

print(solution())