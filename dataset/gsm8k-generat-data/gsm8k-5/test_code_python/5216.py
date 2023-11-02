def solution():
    current_average = (85 + 79 + 92 + 84) / 4  # Calculate Jacob's current average

    # Calculate the score Jacob needs to earn on his fifth test to have an overall average of 85
    required_score = (85 * 5) - (85 + 79 + 92 + 84)

    result = required_score
    return result

print(solution())