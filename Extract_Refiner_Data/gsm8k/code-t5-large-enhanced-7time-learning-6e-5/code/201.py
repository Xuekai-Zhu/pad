def solution():
    
    # Define the scores of the first five tests
    scores = [89, 71, 92, 100, 86]

    # Calculate the total score needed to get an average of 93
    total_score_needed = sum(scores) / 6

    # Calculate the score Brinley needs on the sixth test to get an average of 93
    score_needed_on_sixth_test = (93 - total_score_needed) / 6

    # Display the score Brinley needs on the sixth test
    result = score_needed_on_sixth_test
    return result

print(solution())