def solution():
    # Define the scores for each try
    first_try = 400
    second_try = first_try - 70
    third_try = 2 * second_try

    # Calculate the total score
    total_score = first_try + second_try + third_try
    result = total_score
    return result

print(solution())