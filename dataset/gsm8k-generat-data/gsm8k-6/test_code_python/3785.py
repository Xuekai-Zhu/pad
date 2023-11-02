def solution():
    # Calculate the minimum score Kat needs on her third math test to get an average of 90%
    # We can use the formula: (total score + third test score) / 3 = 90%
    # Rearranging, we get: third test score = (90% * 3) - total score
    total_score = 0.95 + 0.8  # total score from first two tests
    third_test_score = (0.9 * 3) - total_score
    result = third_test_score
    return result

print(solution())