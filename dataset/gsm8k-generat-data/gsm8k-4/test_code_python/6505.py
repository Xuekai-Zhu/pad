def solution():
    """Tatuya, Ivanna, and Dorothy took a quiz together. Tatuya scored twice as much as Ivanna, and Ivanna scored 3/5 times as many marks as Dorothy. If Dorothy scored 90 marks, calculate the average marks scored by the three."""
    # Define the score of Dorothy
    dorothy_score = 90

    # Calculate the score of Ivanna
    ivanna_score = dorothy_score * 3/5

    # Calculate the score of Tatuya
    tatuya_score = ivanna_score * 2

    # Calculate the total score and the average score
    total_score = dorothy_score + ivanna_score + tatuya_score
    average_score = total_score / 3

    result = average_score
    return result

print(solution())