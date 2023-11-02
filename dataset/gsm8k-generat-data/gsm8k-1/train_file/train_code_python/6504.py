def solution():
    """Tatuya, Ivanna, and Dorothy took a quiz together. Tatuya scored twice as much as Ivanna, and Ivanna scored 3/5 times as many marks as Dorothy. If Dorothy scored 90 marks, calculate the average marks scored by the three."""
    dorothy_marks = 90
    ivanna_marks = dorothy_marks * (3/5)
    tatuya_marks = ivanna_marks * 2
    total_marks = dorothy_marks + ivanna_marks + tatuya_marks
    average_marks = total_marks / 3
    result = average_marks
    return result

print(solution())