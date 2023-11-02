def solution():
    """Levi and his brother were playing basketball. Levi had scored 8 times and his brother had scored 12 times. Levi was determined to beat his brother by at least 5 baskets. How many more times does Levi have to score in order to reach his goal if his brother scores another 3 times?"""
    # Define Levi and his brother's scores
    levi_score = 8
    brother_score = 12

    # Define the minimum score difference Levi wants to achieve
    min_score_difference = 5

    # Define the number of additional baskets the brother scores
    additional_brother_baskets = 3

    # Calculate the minimum number of baskets Levi needs to score to reach his goal
    min_levi_baskets = brother_score + additional_brother_baskets + min_score_difference - levi_score

    # return the result
    result = min_levi_baskets
    return result

print(solution())