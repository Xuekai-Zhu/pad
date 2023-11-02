def solution():
    """Tatuya, Ivanna, and Dorothy took a quiz together. Tatuya scored twice as much as Ivanna, and Ivanna scored 3/5 times as many marks as Dorothy. If Dorothy scored 90 marks, calculate the average marks scored by the three."""
    # Calculate Ivanna's score
    ivanna_score = 3/5 * 90

    # Calculate Tatuya's score
    tatuya_score = 2 * ivanna_score

    # Calculate the total marks scored by all three
    total_score = dorothy_score + ivanna_score + tatuya_score

    # Calculate the average score
    average_score = total_score / 3

    # Display the average score
    result = average_score
    return result

print(solution())