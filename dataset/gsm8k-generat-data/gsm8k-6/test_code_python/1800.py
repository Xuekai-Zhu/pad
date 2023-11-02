def solution():
    # Calculate the number of mistakes Leo made
    leo_mistakes = (25 - 1)/2 # Brent scored 1 more mistake than Leo and Madeline got half as many mistakes as Leo
    
    # Calculate Madeline's score
    madeline_score = 25 - 2 - leo_mistakes # Madeline got 2 mistakes less than Brent and Leo
    
    result = madeline_score
    return result

print(solution())