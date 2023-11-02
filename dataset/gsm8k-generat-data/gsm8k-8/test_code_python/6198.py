def solution():
    # Define the scores of Keith, Larry, and Danny
    keith_score = 3
    larry_score = 3 * keith_score
    danny_score = larry_score + 5

    # Calculate the total score
    total_score = keith_score + larry_score + danny_score
    result = total_score
    return result

print(solution())