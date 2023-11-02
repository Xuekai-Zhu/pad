def solution():
    dorothy_score = 90
    ivanna_score = dorothy_score * (3 / 5)
    tatuya_score = ivanna_score * 2

    # Calculate the total score of all three
    total_score = dorothy_score + ivanna_score + tatuya_score

    # Calculate the average score
    average_score = total_score / 3
    result = average_score
    return result

print(solution())