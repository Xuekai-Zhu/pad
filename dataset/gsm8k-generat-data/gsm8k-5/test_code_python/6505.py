def solution():
    dorothy_score = 90
    ivanna_score = 3/5 * dorothy_score
    tatuya_score = 2 * ivanna_score

    # Calculate the total marks scored by the three
    total_score = dorothy_score + ivanna_score + tatuya_score

    # Calculate the average marks scored by the three
    average_score = total_score/3
    result = average_score
    return result

print(solution())