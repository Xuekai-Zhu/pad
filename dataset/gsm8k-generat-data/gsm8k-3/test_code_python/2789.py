def solution():
    """Maria's test scores are 80, 70, and 90. What score does she need to get on a fourth test so that her average score for the four tests is exactly 85?"""
    # Determine Maria's current total score
    current_total = 80 + 70 + 90

    # Determine the score needed for an average of 85
    needed_total = 85 * 4

    # Determine the score needed on the fourth test
    needed_score = needed_total - current_total

    # Display the needed score
    result = needed_score
    return result

print(solution())