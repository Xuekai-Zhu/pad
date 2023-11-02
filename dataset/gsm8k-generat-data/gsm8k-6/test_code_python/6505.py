def solution():
    # Find Ivanna's score
    ivanna_score = (3/5) * 90
    
    # Find Tatuya's score
    tatuya_score = 2 * ivanna_score
    
    # Calculate the total marks scored by the three
    total_marks = dorothy_score + ivanna_score + tatuya_score
    
    # Calculate the average marks
    average_marks = total_marks/3
    
    result = average_marks
    return result

print(solution())