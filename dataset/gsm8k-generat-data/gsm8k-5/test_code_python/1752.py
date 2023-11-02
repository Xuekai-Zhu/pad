def solution():
    total_questions = 50
    
    # Calculate Jose's score
    jose_score = (total_questions - 5) * 2
    
    # Calculate Alisson's score
    alisson_score = jose_score - 40
    
    # Calculate Meghan's score
    meghan_score = jose_score - 20
    
    # Calculate the total score for the three
    total_score = jose_score + alisson_score + meghan_score
    result = total_score
    return result

print(solution())