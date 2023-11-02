def solution():
    """Levi and his brother were playing basketball. Levi had scored 8 times and his brother had scored 12 times. Levi was determined to beat his brother by at least 5 baskets. How many more times does Levi have to score in order to reach his goal if his brother scores another 3 times?"""
    # Define Levi's current score and his brother's current score
    levi_score = 8
    brother_score = 12

    # Determine Levi's goal score
    goal_score = brother_score + 5

    # Determine how many more times Levi needs to score to reach his goal
    more_scores_needed = goal_score - (levi_score + 3)

    # Display how many more times Levi needs to score
    result = more_scores_needed
    return result

print(solution())