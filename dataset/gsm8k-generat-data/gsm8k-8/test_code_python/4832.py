def solution():
    # Define Lowella's score
    lowella_score = 0.35 * 100

    # Define Pamela's score as 20% more than Lowella's score
    pamela_score = lowella_score * 1.2

    # Define Mandy's score as twice Pamela's score
    mandy_score = pamela_score * 2

    result = mandy_score
    return result

print(solution())