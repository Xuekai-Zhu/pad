def solution():
    tatuya_marks = 2 * ivanna_marks
    ivanna_marks = (3/5) * dorothy_marks
    total_marks = tatuya_marks + ivanna_marks + dorothy_marks
    average_marks = total_marks / 3
    return average_marks

print(solution())