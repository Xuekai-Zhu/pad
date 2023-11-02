def solution():
    """To make a yellow score mixture, Taylor has to combine white and black scores in the ratio of 7:6. If she got 78 yellow scores, what's 2/3 of the difference between the number of black and white scores she used?"""
    # Set up the ratio of white scores to black scores
    white_to_black = 7/6
    
    # Calculate the total number of parts in the ratio
    total_parts = white_to_black + 1
    
    # Calculate the number of parts that represent the yellow scores
    yellow_parts = 7 + 6
    
    # Calculate the total number of scores used to make the yellow mixture
    total_scores = yellow_parts / total_parts * 78
    
    # Calculate the number of black scores used in the mixture
    black_scores = total_scores / total_parts * 6
    
    # Calculate the number of white scores used in the mixture
    white_scores = total_scores / total_parts * 7
    
    # Calculate the difference between the number of black and white scores used
    score_difference = black_scores - white_scores
    
    # Calculate 2/3 of the score difference
    result = score_difference * 2/3
    return result

print(solution())