def solution():
    current_total = 80 + 70 + 90  # Add up Maria's current test scores
    current_num_tests = 3  # Maria has taken 3 tests so far
    desired_average = 85  # Maria wants her overall average to be 85
    num_tests_needed = 4  # Maria needs to take 4 tests in total

    # Calculate the minimum score Maria needs on the fourth test to get an average of 85
    required_score = (desired_average * num_tests_needed) - current_total
    required_score /= (num_tests_needed - current_num_tests)

    result = required_score
    return result

print(solution())