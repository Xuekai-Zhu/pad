def solution():
    # Calculate the current total of Jacob's scores
    current_total = 85 + 79 + 92 + 84

    # Calculate the number of tests Jacob has taken
    num_tests = 4

    # Calculate the minimum score Jacob needs on his fifth test to have an overall average of 85
    min_fifth_test_score = (85*num_tests + x) / (num_tests+1) - current_total/num_tests

    result = min_fifth_test_score
    return result

print(solution())