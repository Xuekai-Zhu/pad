def solution():
    # Calculate the average of Jacob's first four tests
    first_four_avg = (85 + 79 + 92 + 84) / 4

    # Calculate the score Jacob needs on his fifth test to have an overall average of 85
    fifth_score_needed = (85 * 5) - (first_four_avg * 4)
    result = fifth_score_needed
    return result

print(solution())