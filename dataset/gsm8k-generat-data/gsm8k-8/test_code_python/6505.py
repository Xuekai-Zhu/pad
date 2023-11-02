def solution():
    # Define the score ratio between Ivanna and Dorothy
    ivanna_to_dorothy_ratio = 3/5

    # Calculate Ivanna's score
    dorothy_score = 90
    ivanna_score = ivanna_to_dorothy_ratio * dorothy_score

    # Calculate Tatuya's score
    tatuya_score = 2 * ivanna_score

    # Calculate the total score and the average score
    total_score = dorothy_score + ivanna_score + tatuya_score
    average_score = total_score / 3
    result = average_score
    return result

print(solution())